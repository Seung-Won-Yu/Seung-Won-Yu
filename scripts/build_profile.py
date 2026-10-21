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
KOREAN = "'Apple SD Gothic Neo', 'Malgun Gothic', Arial, sans-serif"
SERIF = "Georgia, 'Times New Roman', serif"


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
    bg, ink, muted, edge, blue, wash = ('#101D2C','#F1F5FA','#AEBED2','#2B3D52','#7CA7FF','#203B60') if dark else ('#F0F3F7','#112940','#4D647C','#CDD8E4','#245EDB','#D5E3FA')
    w,h = (640,700) if mobile else (1200,540)
    s = start(w,h,'Seung-Won Yu — AI systems, web products & games.','유승원. AI 도구와 웹 제품, 플레이할 수 있는 세계를 만듭니다. Ash & Amber의 실제 여덟 동작 프레임으로 캐릭터가 한 걸음 움직인 뒤 잠시 쉽니다. 동작 줄이기 설정에서는 정지합니다.')
    s += f'<defs><clipPath id="hero-edge"><rect width="{w}" height="{h}" rx="18"/></clipPath></defs><g clip-path="url(#hero-edge)"><rect width="{w}" height="{h}" fill="{bg}"/>'
    if mobile:
        s += text(38,47,'유승원',21,muted,600,font=KOREAN)
        s += text(34,136,'Seung-Won',77,ink,750,'letter-spacing="-4.4"')
        s += text(32,231,'Yu.',106,ink,750,'letter-spacing="-5.6"')
        s += text(39,282,'AI systems, web products & games.',23,muted)
        s += text(39,329,'AI 도구와 웹 제품,',25,ink,500,font=KOREAN)
        s += text(39,366,'플레이할 수 있는 세계를 만듭니다.',25,ink,500,font=KOREAN)
        s += f'<path d="M322 649V511a135 135 0 0 1 270 0v138z" fill="{wash}"/>'
        s += f'<path d="M325 649h266M335 624h246M346 600h224M375 580h164M457 571v78M409 576l-26 73M505 576l26 73" stroke="{blue}" opacity=".23" fill="none"/>'
        s += f'<ellipse cx="458" cy="642" rx="116" ry="9" fill="{blue}" opacity=".13"/>'
        s += character(458,641,1.03)
        s += f'<path d="M40 440h160" stroke="{blue}" opacity=".5"/>'
        s += text(40,487,'Design.',29,ink,600)
        s += text(40,530,'Build.',29,ink,600)
        s += text(40,573,'Verify.',29,ink,600)
        s += text(394,680,'Ash & Amber',16,muted)
    else:
        s += text(57,58,'유승원',21,muted,600,font=KOREAN)
        s += text(49,166,'Seung-Won',96,ink,750,'letter-spacing="-5.7"')
        s += text(47,278,'Yu.',122,ink,750,'letter-spacing="-6.5"')
        s += text(58,337,'AI systems, web products & games.',25,muted)
        s += text(58,398,'AI 도구와 웹 제품,',25,ink,500,font=KOREAN)
        s += text(58,436,'플레이할 수 있는 세계를 만듭니다.',25,ink,500,font=KOREAN)
        s += f'<path d="M736 462V258a204 204 0 0 1 408 0v204z" fill="{wash}"/>'
        s += f'<path d="M736 462h408M751 428h378M776 394h328M811 361h258M940 344v118M877 350l-46 112M1003 350l46 112M843 361l-107 101M1037 361l107 101" fill="none" stroke="{blue}" opacity=".23"/>'
        s += f'<ellipse cx="938" cy="452" rx="142" ry="11" fill="{blue}" opacity=".14"/>'
        s += character(932,450,1.37)
        s += text(861,500,'Ash & Amber',18,muted)
        s += text(58,500,'Design. Build. Verify.',18,muted)
    return s + f'</g><rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="18" fill="none" stroke="{edge}"/></svg>\n'


def showcases():
    s = start(1200,600,'autolabel — from input to review','실제 DeepPCB 샘플과 autolabel의 모델 초안·검수 화면. 입력, 모델 초안, 예외 검수, 전용 모델 학습으로 이어지는 흐름.')
    s += '<defs><clipPath id="edge"><rect width="1200" height="600" rx="16"/></clipPath></defs><g clip-path="url(#edge)"><rect width="1200" height="600" fill="#102D35"/>'
    s += text(38,49,'Image in. Review out.',29,'#E9F9F4',600)
    s += text(917,48,'Local AI workflow',20,'#A0C6C2')
    s += '<rect x="38" y="89" width="330" height="330" rx="9" fill="#D9E7E3"/>' + image('pcb-sample.png',38,89,330,330)
    s += '<path d="M389 252h25m-9-9 9 9-9 9" stroke="#7EE4C8" stroke-width="2" fill="none"/>'
    s += crop('autolabel.png',438,89,724,410,'515 122 640 441',(1200,630))
    s += text(38,461,'실제 PCB 결함 샘플',20,'#A0C6C2',font=KOREAN)
    s += '<path d="M38 526h1124" stroke="#32535A"/>'
    s += text(38,569,'입력',23,'#E9F9F4',500,font=KOREAN)+text(257,569,'모델 초안',23,'#E9F9F4',500,font=KOREAN)+text(560,569,'예외 검수',23,'#E9F9F4',500,font=KOREAN)+text(888,569,'전용 모델 학습',23,'#E9F9F4',500,font=KOREAN)
    s += '<path d="M161 561h48m-8-7 8 7-8 7M450 561h56m-8-7 8 7-8 7M763 561h70m-8-7 8 7-8 7" stroke="#7EE4C8" stroke-width="1.5" fill="none"/>'
    yield 'autolabel',s+'</g></svg>\n'

    s = start(1200,750,'Workroom Portal — personal to shared','조직과 구성원 식별자를 예시 값으로 바꾼 공개판의 실제 관리자 대시보드. 개인 작업에서 팀 공유와 관리자 점검으로 이어지는 포털.')
    s += '<defs><clipPath id="screen"><rect x="25" y="72" width="1150" height="647" rx="9"/></clipPath></defs><rect width="1200" height="750" rx="16" fill="#DCE5F2"/>'
    s += text(28,45,'Personal / Shared / Admin',26,'#193C67',600)
    s += text(973,44,'Public preview',20,'#4A6284')
    s += '<g clip-path="url(#screen)">'+image('workroom.png',25,72,1150,647)+'</g></svg>\n'
    yield 'workroom-portal',s

    s = start(1200,700,'PocketDesk OS — a desktop that remembers','실제 PocketDesk OS 화면. 브라우저 안에서 창과 파일을 다루고, 창·파일·테마 상태를 보존하는 데스크톱.')
    s += '<defs><clipPath id="screen"><rect x="25" y="72" width="1150" height="604" rx="9"/></clipPath></defs><rect width="1200" height="700" rx="16" fill="#C9D8EC"/>'
    s += text(28,45,'A desktop that remembers.',26,'#173853',600)
    s += text(926,44,'Browser-native OS',20,'#435F7C')
    s += '<g clip-path="url(#screen)">'+image('pocketdesk.png',25,72,1150,604)+'</g></svg>\n'
    yield 'pocket-desk-os',s

    s = start(1200,620,'Ash & Amber — Rune Drift Survivors','실제 게임 원화와 전투 화면. 동료를 고르고, 무기를 진화시키고, 숲의 보스에 도전하는 한 판 5분의 2D 브라우저 게임.')
    s += '<defs><clipPath id="edge"><rect width="1200" height="620" rx="16"/></clipPath><linearGradient id="shade"><stop stop-color="#102C29" stop-opacity=".96"/><stop offset="1" stop-color="#102C29" stop-opacity=".4"/></linearGradient><clipPath id="combat"><rect x="542" y="178" width="610" height="343" rx="10"/></clipPath></defs><g clip-path="url(#edge)">'
    s += image('forest.webp',0,0,1200,620,'preserveAspectRatio="xMidYMid slice"')+'<rect width="1200" height="620" fill="url(#shade)"/>'
    s += text(42,56,'Rune Drift Survivors',23,'#ECDBB6',500)
    s += text(35,162,'Ash &',85,'#FFF0CD',600,'letter-spacing="-3"',SERIF)+text(35,253,'Amber',85,'#FFF0CD',600,'letter-spacing="-3"',SERIF)
    s += text(42,302,'한 판 5분, 한 번 더.',23,'#E8DDBE',font=KOREAN)
    s += image('ash-portrait.webp',235,288,193,289)
    s += '<rect x="536" y="172" width="622" height="355" rx="15" fill="#122820" stroke="#BCA275"/>'
    s += '<g clip-path="url(#combat)">'+image('combat.jpg',542,178,610,343)+'</g>'
    s += text(42,574,'동료 선택 · 무기 진화 · 보스전',22,'#E8DDBE',font=KOREAN)
    s += text(970,574,'Canvas 2D',20,'#D5D8BC')
    yield 'rune-drift-survivors',s+'</g></svg>\n'


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
