"""Build self-contained GitHub profile artwork from unchanged public project assets.

Run with Python 3; no third-party packages or remote requests are required.
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


def character(center, baseline, scale):
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
    for i, (x,y,w,h) in enumerate(ASH_FRAMES):
        left = center - (126 - x % 256) * scale
        s += f'<svg class="ash-pose ash-{i}" x="{left}" y="{baseline-h*scale}" width="{w*scale}" height="{h*scale}" viewBox="{x} {y} {w} {h}" overflow="hidden"><use href="#ash-atlas"/></svg>'
    return s


def hero(dark, mobile):
    ink, muted = ('#F0F6FC','#9DA7B3') if dark else ('#1F2328','#59636E')
    w,h = (640,176) if mobile else (1200,176)
    s = start(w,h,'Seung-Won Yu — AI systems, web products & games.','Seung-Won Yu. AI 도구와 웹 제품, 브라우저 게임을 만듭니다. 작은 Ash & Amber 캐릭터가 한 걸음 움직인 뒤 잠시 쉽니다. 동작 줄이기 설정에서는 정지합니다.')
    if mobile:
        s += text(1,62,'Seung-Won Yu',44,ink,650,'letter-spacing="-1.5"')
        s += text(3,108,'AI systems, web products',24,muted)
        s += text(3,143,'& browser games.',24,muted)
        s += character(567,144,.39)
    else:
        s += text(1,69,'Seung-Won Yu',52,ink,650,'letter-spacing="-1.5"')
        s += text(3,119,'AI systems, web products & browser games.',25,muted)
        s += character(1118,145,.49)
    return s+'</svg>\n'


def showcases():
    # Show the project interfaces, without adding another headline or poster.
    s = start(1200,827,'autolabel — public review preview','autolabel의 공개 검수 미리보기. 모델 초안, PCB 결함 샘플, 검수할 어노테이션을 함께 보여줍니다.')
    s += '<defs><clipPath id="screen"><rect width="1200" height="827" rx="10"/></clipPath></defs><g clip-path="url(#screen)">'
    s += crop('autolabel.png',0,0,1200,827,'515 122 640 441',(1200,630))
    yield 'autolabel',s+'</g></svg>\n'

    s = start(1200,675,'Workroom Portal — public administrator preview','조직과 구성원 식별자를 예시 값으로 바꾼 공개판의 관리자 대시보드.')
    s += '<defs><clipPath id="screen"><rect width="1200" height="675" rx="10"/></clipPath></defs><g clip-path="url(#screen)">'
    yield 'workroom-portal',s+image('workroom.png',0,0,1200,675)+'</g></svg>\n'

    s = start(1200,630,'PocketDesk OS — browser desktop','PocketDesk OS 화면. 창, 파일, 앱과 작업 표시줄을 갖춘 브라우저 데스크톱.')
    s += '<defs><clipPath id="screen"><rect width="1200" height="630" rx="10"/></clipPath></defs><g clip-path="url(#screen)">'
    yield 'pocket-desk-os',s+image('pocketdesk.png',0,0,1200,630)+'</g></svg>\n'

    s = start(1200,675,'Ash & Amber — actual gameplay','Rune Drift Survivors의 Ash & Amber 전투 화면. 한 판 5분의 Canvas 2D 브라우저 생존 게임.')
    s += '<defs><clipPath id="screen"><rect width="1200" height="675" rx="10"/></clipPath></defs><g clip-path="url(#screen)">'
    yield 'rune-drift-survivors',s+image('combat.jpg',0,0,1200,675)+'</g></svg>\n'


if __name__ == '__main__':
    for dark in [False,True]:
        for mobile in [False,True]:
            suffix=('mobile-' if mobile else '')+('dark' if dark else 'light')
            (ASSETS/f'profile-hero-{suffix}.svg').write_text(hero(dark,mobile))
    for name,svg in showcases():
        (ASSETS/'showcase'/f'{name}.svg').write_text(svg)
    paths = list(ASSETS.glob('profile-hero*.svg'))+list((ASSETS/'showcase').glob('*.svg'))
    for path in paths:
        ET.parse(path)
        print(f'{path.relative_to(ROOT)}: {path.stat().st_size // 1024} KiB')
