"""Build self-contained GitHub profile artwork from unchanged public project assets.

Run with Python 3; no third-party packages or remote requests are required.
Publish generated assets first, then pin README image URLs to that commit.
Immutable image URLs avoid stale GitHub raw-branch image caches.
"""
from base64 import b64encode
from html import escape
from pathlib import Path
import mimetypes
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
SOURCE = ASSETS / "source"
SANS = "Arial, 'Helvetica Neue', sans-serif"
KOREAN = "Arial, 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif"


def image(name, x, y, width, height, extra=""):
    path = SOURCE / name
    uri = f"data:{mimetypes.guess_type(path)[0]};base64,{b64encode(path.read_bytes()).decode()}"
    return f'<image x="{x}" y="{y}" width="{width}" height="{height}" href="{uri}" {extra}/>'


def text(x, y, value, size, color, weight=400, extra="", font=SANS):
    return f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" font-weight="{weight}" fill="{color}" {extra}>{escape(value)}</text>'


def start(width, height, title, description):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(description)}</desc>'


def crop(name, x, y, width, height, viewbox, source_size):
    return f'<svg x="{x}" y="{y}" width="{width}" height="{height}" viewBox="{viewbox}" preserveAspectRatio="xMidYMid slice">' + image(name, 0, 0, *source_size) + '</svg>'


# Measured source bounds from rune-drift-survivors/src/survivor/actor-art.js.
# Use the same scale and foot baseline for every pose; do not stretch paintings.
ASH_FRAMES = [(13,21,236,239),(273,28,223,233),(531,20,223,242),(774,15,234,244),
              (12,279,236,238),(271,284,227,234),(531,281,222,237),(769,272,238,246)]


def character(center, baseline, scale, face_left=False):
    css = []
    for i in range(8):
        begin, end = i * 5, (i + 1) * 5
        if i == 0:
            frames = '0%,4.999%{opacity:1}5%,39.999%{opacity:0}40%,100%{opacity:1}'
        else:
            frames = f'0%,{begin-.001}%{{opacity:0}}{begin}%,{end-.001}%{{opacity:1}}{end}%,100%{{opacity:0}}'
        css.append(f'.ash-{i}{{opacity:{1 if i == 0 else 0};animation:ash-{i} 3.2s steps(1,end) infinite}}@keyframes ash-{i}{{{frames}}}')
    css.append('@media(prefers-reduced-motion:reduce){.ash-pose{animation:none!important;opacity:0}.ash-0{opacity:1}}')
    s = '<style>' + ''.join(css) + '</style><defs>' + image('ash-motion.webp',0,0,1024,1536,'id="ash-atlas"') + '</defs>'
    if face_left:
        s += f'<g transform="translate({center*2} 0) scale(-1 1)">'
    for i, (x,y,w,h) in enumerate(ASH_FRAMES):
        left = center - (126 - x % 256) * scale
        s += f'<svg class="ash-pose ash-{i}" x="{left}" y="{baseline-h*scale}" width="{w*scale}" height="{h*scale}" viewBox="{x} {y} {w} {h}" overflow="hidden"><use href="#ash-atlas"/></svg>'
    if face_left:
        s += '</g>'
    return s


def hero(dark, mobile):
    # Keep one navy scene in both themes, with transparent space outside its
    # frame for the character. All original project artwork stays unchanged.
    ink,muted,blue = '#EDF5FF','#AABFD9','#7DBEFF'
    edge = '#315984' if dark else '#294B74'
    w,h = (640,620) if mobile else (1200,420)
    s = start(w,h,'Seung-Won Yu — AI systems, web products & games.',
              'Seung-Won Yu. AI 도구와 웹 제품, 브라우저 게임을 만들고 실제 동작과 검증 기록을 남깁니다. '
              'AI: 검수와 전용 모델 학습. Web: 상태 저장과 오프라인. Games: 5분 로그라이트. '
              '네이비·블루 배너의 프레임 밖으로 큰 Ash & Amber 캐릭터가 나옵니다. '
              '푸른 빛과 앰버 포인트가 흐르고 캐릭터가 한 걸음 움직인 뒤 쉽니다. 동작 줄이기 설정에서는 정지합니다.')
    s += '''<defs>
      <linearGradient id="navy-scene" x1="0" y1="0" x2="1" y2=".5"><stop stop-color="#0C1729"/><stop offset=".57" stop-color="#102746"/><stop offset="1" stop-color="#173B64"/></linearGradient>
      <radialGradient id="blue-light"><stop stop-color="#3A91F0" stop-opacity=".38"/><stop offset="1" stop-color="#3A91F0" stop-opacity="0"/></radialGradient>
      <radialGradient id="amber-light"><stop stop-color="#F4B34F" stop-opacity=".28"/><stop offset="1" stop-color="#F4B34F" stop-opacity="0"/></radialGradient>
      <linearGradient id="portal-edge" x1="0" y1="1" x2="1" y2="0"><stop stop-color="#37689B" stop-opacity=".15"/><stop offset=".6" stop-color="#80BFFF" stop-opacity=".85"/><stop offset="1" stop-color="#F2B45F" stop-opacity=".55"/></linearGradient>
    </defs>
    <style>
      .scene-flow{stroke-dasharray:36 440;animation:scene-flow 12s linear infinite}
      .scene-spark{animation:scene-spark 6s ease-in-out infinite}
      @keyframes scene-flow{to{stroke-dashoffset:-952}}
      @keyframes scene-spark{0%,100%{opacity:.35}50%{opacity:1}}
      @media(prefers-reduced-motion:reduce){.scene-flow,.scene-spark{animation:none!important}}
    </style>'''
    if mobile:
        s += f'<rect x="8.5" y="36.5" width="600" height="566" rx="24" fill="url(#navy-scene)" stroke="{edge}"/>'
        s += '<ellipse cx="470" cy="442" rx="230" ry="205" fill="url(#blue-light)"/>'
        s += '<path d="M344 580V441a119 119 0 0 1 238 0v139" fill="#234D7E" fill-opacity=".13" stroke="url(#portal-edge)" stroke-width="2"/>'
        s += '<path d="M31 62H570M31 62V80M33 314H238L266 342V556H326M32 588H270L310 548" fill="none" stroke="#4B7CAC" stroke-opacity=".3"/>'
        s += '<path class="scene-flow" d="M32 588H270L310 548H540" fill="none" stroke="#72B7FF" stroke-width="2" opacity=".7"/>'
        s += '<path d="M9 112V64a27 27 0 0 1 27-27h63M535 603h47a27 27 0 0 0 27-27v-47" fill="none" stroke="#DCA75F" stroke-width="2" opacity=".8"/>'
        s += text(36,129,'Seung-Won Yu',52,ink,650,'letter-spacing="-1.7"')
        s += text(38,173,'AI systems, web products & games.',23,blue)
        s += text(38,225,'AI 도구·웹 제품·게임을 만들고,',27,ink,font=KOREAN)
        s += text(38,263,'실제 동작과 검증 기록을 남깁니다.',27,ink,font=KOREAN)
        for y,label,description in [(374,'AI','검수·모델 학습'),(454,'Web','저장·오프라인'),(534,'Games','5분 로그라이트')]:
            s += text(38,y,label,25,blue,600)
            s += text(38,y+32,description,24,muted,font=KOREAN)
        s += '<ellipse cx="384" cy="538" rx="91" ry="80" fill="url(#amber-light)"/>'
        s += '<ellipse cx="482" cy="608" rx="110" ry="8" fill="#030B18" opacity=".45"/>'
        s += character(476,610,1.16,face_left=True)
        s += '<g class="scene-spark" fill="#F2B45F"><path d="m588 281 3 8 8 3-8 3-3 8-3-8-8-3 8-3Z"/><circle cx="309" cy="354" r="2"/><circle cx="576" cy="542" r="2"/></g>'
    else:
        s += f'<rect x="8.5" y="68.5" width="1150" height="322" rx="24" fill="url(#navy-scene)" stroke="{edge}"/>'
        s += '<ellipse cx="971" cy="232" rx="290" ry="220" fill="url(#blue-light)"/>'
        s += '<path d="M812 371V228a157 157 0 0 1 314 0v143" fill="#376AA3" fill-opacity=".09" stroke="url(#portal-edge)" stroke-width="2"/>'
        s += '<path d="M841 371V228a128 128 0 0 1 256 0v143" fill="none" stroke="#5D9DDD" stroke-opacity=".22"/>'
        s += '<path d="M35 94H616L662 140H790M35 94V120M608 365H690L738 317H806M774 390 885 310M915 390 945 310M1056 390 1005 310M1158 390 1065 310M790 363H1158M824 337H1123" fill="none" stroke="#5B90C4" stroke-opacity=".24"/>'
        s += '<path class="scene-flow" d="M35 94H616L662 140H790" fill="none" stroke="#78B9FF" stroke-width="2" opacity=".7"/>'
        s += '<path d="M9 140V96a27 27 0 0 1 27-27h58M1070 391h62a27 27 0 0 0 27-27v-40" fill="none" stroke="#DCA75F" stroke-width="2" opacity=".9"/>'
        s += text(48,169,'Seung-Won Yu',66,ink,650,'letter-spacing="-2.1"')
        s += text(50,213,'AI systems, web products & browser games.',25,blue)
        s += text(50,267,'AI 워크플로부터 웹 인터페이스와 게임까지,',25,ink,font=KOREAN)
        s += text(50,305,'직접 써볼 수 있는 제품과 검증 기록을 만듭니다.',25,ink,font=KOREAN)
        s += '<path d="M50 353h24" stroke="#F2B45F" stroke-width="2"/>'
        s += text(88,360,'Design. Build. Verify.',20,muted)
        s += '<ellipse cx="837" cy="316" rx="115" ry="103" fill="url(#amber-light)"/>'
        s += '<ellipse cx="983" cy="402" rx="164" ry="10" fill="#030B18" opacity=".45"/>'
        s += character(975,402,1.58,face_left=True)
        s += '<g class="scene-spark" fill="#F2B45F"><path d="m1136 118 3 9 9 3-9 3-3 9-3-9-9-3 9-3Z"/><path d="m772 229 2 6 6 2-6 2-2 6-2-6-6-2 6-2Z"/><circle cx="740" cy="97" r="2"/><circle cx="1113" cy="332" r="2"/></g>'
    return s+'</svg>\n'

def showcases():
    # A common 8:5 canvas and a 640px display cap avoid enlarging the
    # 640px-wide autolabel source. Contain every interface, without cutting UI.
    previews = [
        ('autolabel','autolabel.png',(1200,630),'515 122 640 441',
         'autolabel — public review preview',
         '공개 검수 미리보기. 모델 초안, PCB 결함 샘플과 검수할 어노테이션.'),
        ('workroom-portal','workroom.png',(1672,941),'0 0 1672 941',
         'Workroom Portal — public administrator preview',
         '조직과 구성원 식별자를 예시 값으로 바꾼 공개판의 관리자 대시보드.'),
        ('pocket-desk-os','pocketdesk.png',(1200,630),'0 0 1200 630',
         'PocketDesk OS — browser desktop',
         '창, 파일, 앱과 작업 표시줄을 갖춘 브라우저 데스크톱.'),
        ('rune-drift-survivors','combat.jpg',(1280,720),'0 0 1280 720',
         'Ash & Amber — actual gameplay',
         '한 판 5분의 Canvas 2D 브라우저 게임 Ash & Amber의 전투 화면.'),
    ]
    for name, source, size, viewbox, title, description in previews:
        s = start(960,600,title,description)
        s += '<rect x=".5" y=".5" width="959" height="599" rx="12" fill="#10151D" stroke="#28323F"/>'
        s += '<svg x="16" y="16" width="928" height="568" viewBox="'+viewbox+'" preserveAspectRatio="xMidYMid meet">'
        s += image(source,0,0,*size)+'</svg></svg>\n'
        yield name,s


PROJECTS = [
    dict(name='autolabel', source='autolabel.png', size=(1200,630), viewbox='515 122 640 441',
         label='PCB 검출 모델 평가', metric='0.963', metric_size=76,
         support='mAP50 · 승인 데이터 300장',
         note='고정 홀드아웃 / M4 Pro · MPS', foot='단일 머신에서 자체 측정',
         preview='공개 검수 미리보기', accent='#69B7FF', light_accent='#0969DA'),
    dict(name='workroom-portal', source='workroom.png', size=(1672,941), viewbox='0 0 1672 941',
         label='에이전트 작업공간의 접근 제어', metric='명시적 공유', metric_size=54,
         support='개인 → 팀 공유 → 관리자',
         note='권한·경로·스트리밍 회귀 점검', foot='공유한 결과만 팀 작업공간으로',
         preview='공개판 관리자 대시보드', accent='#69B7FF', light_accent='#0969DA'),
    dict(name='pocket-desk-os', source='pocketdesk.png', size=(1200,630), viewbox='0 0 1200 630',
         label='브라우저 안의 데스크톱', metric='17개 앱', metric_size=62,
         support='9단계 QA 게이트',
         note='브라우저 흐름 / ARIA·포커스', foot='파일·ZIP부터 오프라인 재실행까지',
         preview='PocketDesk OS 실행 화면', accent='#69B7FF', light_accent='#0969DA'),
    dict(name='rune-drift-survivors', source='combat.jpg', size=(1280,720), viewbox='0 0 1280 720',
         label='전투 모멘텀 패스의 검증 기록', metric='75 unit', metric_size=62,
         support='20 browser 테스트',
         note='데스크톱 브라우저 3개 viewport', foot='한 판 5분의 Canvas 2D 로그라이트',
         preview='Ash & Amber 실제 전투 화면', accent='#69B7FF', light_accent='#0969DA'),
]


def feature(project, dark, mobile):
    """A full-width preview and outcome, side by side or stacked on phones.

    Keep the complete interface inside its viewport. At normal GitHub widths,
    even the smallest (640px) source region is displayed below its native size.
    Text is repeated in native README prose for search and text accessibility.
    """
    w,h = (640,688) if mobile else (1200,388)
    ink,muted,line,bg = ('#F0F6FC','#AAB4C0','#303A47','#151B23') if dark else ('#1F2328','#59636E','#D1D9E0','#F6F8FA')
    accent = project['accent'] if dark else project['light_accent']
    s = start(w,h,project['preview']+' — '+project['metric'],
              '。'.join(project[k] for k in ['label','metric','support','note','foot']))
    s += f'<rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="10" fill="{bg}" stroke="{line}"/>'
    px,py,pw,ph = (14,14,612,344) if mobile else (14,14,640,360)
    s += f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="4" fill="#10151D"/>'
    s += f'<svg x="{px}" y="{py}" width="{pw}" height="{ph}" viewBox="{project["viewbox"]}" preserveAspectRatio="xMidYMid meet">'
    s += image(project['source'],0,0,*project['size'])+'</svg>'
    if mobile:
        x=28
        s += text(x,410,project['label'],27,muted,font=KOREAN)
        s += text(x,484,project['metric'],min(project['metric_size'],64),ink,650,font=KOREAN)
        s += text(x,537,project['support'],32,accent,600,font=KOREAN)
        s += f'<path d="M28 565H612" stroke="{line}"/>'
        s += text(x,611,project['note'],26,muted,font=KOREAN)
        s += text(x,654,project['foot'],26,muted,font=KOREAN)
    else:
        x=698
        s += text(x,68,project['label'],24,muted,font=KOREAN)
        s += text(x,159,project['metric'],project['metric_size'],ink,650,font=KOREAN)
        s += text(x,212,project['support'],29,accent,600,font=KOREAN)
        s += f'<path d="M698 246H1168" stroke="{line}"/>'
        s += text(x,294,project['note'],23,muted,font=KOREAN)
        s += text(x,335,project['foot'],23,muted,font=KOREAN)
    return s+'</svg>\n'


if __name__ == '__main__':
    for dark in [False,True]:
        for mobile in [False,True]:
            suffix=('mobile-' if mobile else '')+('dark' if dark else 'light')
            (ASSETS/f'profile-hero-{suffix}.svg').write_text(hero(dark,mobile))
    for name,svg in showcases():
        (ASSETS/'showcase'/f'{name}.svg').write_text(svg)
    (ASSETS/'features').mkdir(exist_ok=True)
    for project in PROJECTS:
        for dark in [False,True]:
            for mobile in [False,True]:
                suffix=('mobile-' if mobile else '')+('dark' if dark else 'light')
                (ASSETS/'features'/f'{project["name"]}-{suffix}.svg').write_text(feature(project,dark,mobile))
    paths = list(ASSETS.glob('profile-hero*.svg'))+list((ASSETS/'showcase').glob('*.svg'))+list((ASSETS/'features').glob('*.svg'))
    for path in paths:
        ET.parse(path)
        print(f'{path.relative_to(ROOT)}: {path.stat().st_size // 1024} KiB')
