"""Fetch public GitHub aggregates and optionally publish only activity artifacts.

Requires Python 3 and authenticated gh. Daily runs use the repository's existing
GITHUB_TOKEN; no personal token or private-repository access is requested.
The generated profile-stats branch is separate from the portfolio's main branch.
"""
import argparse
from datetime import datetime, timedelta, timezone
import json
import os
from pathlib import Path
import subprocess
import tempfile
import xml.etree.ElementTree as ET

from build_profile import ROOT, activity

OWNER='Seung-Won-Yu'
REPOSITORY='Seung-Won-Yu/Seung-Won-Yu'
BRANCH='profile-stats'
OUTPUT=ROOT/'assets'/'activity'
QUERY='''query($login: String!, $cursor: String, $from: DateTime!, $to: DateTime!) {
  user(login: $login) {
    login
    repositories(first: 100, after: $cursor, privacy: PUBLIC, ownerAffiliations: OWNER) {
      totalCount nodes { stargazerCount } pageInfo { hasNextPage endCursor }
    }
    contributionsCollection(from: $from, to: $to) {
      startedAt endedAt contributionCalendar { totalContributions }
    }
  }
}'''


def command(args, *, env=None, input=None):
    result=subprocess.run(args,cwd=ROOT,env=env,input=input,text=True,capture_output=True)
    if result.returncode:
        raise RuntimeError(f'{args[0]} failed: {result.stderr.strip()}')
    return result.stdout.strip()


def nonnegative(value):
    if type(value) is not int or value<0:
        raise ValueError('GitHub returned an invalid activity count')
    return value


def fetch_stats():
    now=datetime.now(timezone.utc).replace(microsecond=0)
    variables=dict(login=OWNER,cursor=None,
                   **{'from':(now-timedelta(days=365)).isoformat(),'to':now.isoformat()})
    stars=0
    seen=set()
    first=None
    while True:
        response=json.loads(command(['gh','api','graphql','--input','-'],
                                    input=json.dumps(dict(query=QUERY,variables=variables))))
        if response.get('errors'):
            raise RuntimeError('GitHub GraphQL could not complete the activity query')
        user=response['data']['user']
        if user['login'].casefold()!=OWNER.casefold():
            raise ValueError('Unexpected GitHub profile in activity response')
        repos=user['repositories']
        if first is None:
            first=user
        stars+=sum(nonnegative(repo['stargazerCount']) for repo in repos['nodes'])
        page=repos['pageInfo']
        if not page['hasNextPage']:
            break
        cursor=page['endCursor']
        if not cursor or cursor in seen:
            raise ValueError('GitHub repository pagination did not advance')
        seen.add(cursor)
        variables['cursor']=cursor
    collection=first['contributionsCollection']
    return dict(source='https://github.com/'+OWNER,
                fetched_at=now.isoformat(),
                as_of_date=now.astimezone(timezone(timedelta(hours=9))).strftime('%Y.%m.%d'),
                period_start=collection['startedAt'],period_end=collection['endedAt'],
                contributions_last_year=nonnegative(collection['contributionCalendar']['totalContributions']),
                public_repositories=nonnegative(first['repositories']['totalCount']),
                stars_received=stars)


def render(stats):
    artifacts={'stats.json':json.dumps(stats,ensure_ascii=False,indent=2)+'\n'}
    for dark in [False,True]:
        for mobile in [False,True]:
            suffix=('mobile-' if mobile else '')+('dark' if dark else 'light')
            svg=activity(stats,dark,mobile)
            ET.fromstring(svg)
            artifacts['activity-'+suffix+'.svg']=svg
    OUTPUT.mkdir(parents=True,exist_ok=True)
    for name,content in artifacts.items():
        (OUTPUT/name).write_text(content,encoding='utf-8')
    return [str((OUTPUT/name).relative_to(ROOT)) for name in artifacts]


def publish(files,date):
    # Git's temporary index stages exactly five generated artifacts. Neither
    # the working branch nor the user's regular index is checked out or reset.
    git=['git','-c','credential.helper=','-c','credential.helper=!gh auth git-credential']
    origin=command(['git','remote','get-url','origin'])
    if origin not in ['https://github.com/'+REPOSITORY+'.git',
                      'https://github.com/'+REPOSITORY,
                      'git@github.com:'+REPOSITORY+'.git']:
        raise ValueError('Refusing to publish activity to an unexpected repository')
    remote=command(git+['ls-remote','--heads','origin','refs/heads/'+BRANCH])
    parent=None
    if remote:
        command(git+['fetch','--no-tags','--depth=1','origin','refs/heads/'+BRANCH])
        parent=command(['git','rev-parse','FETCH_HEAD'])
    with tempfile.TemporaryDirectory(prefix='profile-activity-index-') as folder:
        env=os.environ.copy()
        env['GIT_INDEX_FILE']=str(Path(folder)/'index')
        for role in ['AUTHOR','COMMITTER']:
            env['GIT_'+role+'_NAME']='github-actions[bot]'
            env['GIT_'+role+'_EMAIL']='41898282+github-actions[bot]@users.noreply.github.com'
        command(['git','read-tree','--empty'],env=env)
        command(['git','add','-f','--',*files],env=env)
        tree=command(['git','write-tree'],env=env)
        if parent and tree==command(['git','rev-parse',parent+'^{tree}']):
            return parent
        args=['git','commit-tree',tree]
        if parent:
            args+=['-p',parent]
        commit=command(args,env=env,input='Refresh public profile activity ('+date+')\n')
        command(git+['push','origin',commit+':refs/heads/'+BRANCH])
    return commit


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--publish',action='store_true',help='Push the five generated files to profile-stats')
    args=parser.parse_args()
    stats=fetch_stats()
    files=render(stats)
    if args.publish:
        stats['published_commit']=publish(files,stats['as_of_date'])
    print(json.dumps(stats,ensure_ascii=False))


if __name__=='__main__':
    main()
