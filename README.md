<picture>
  <source media="(prefers-color-scheme: dark) and (max-width: 600px)" srcset="./assets/profile-hero-mobile-dark.svg?v=studio-20261021" />
  <source media="(max-width: 600px)" srcset="./assets/profile-hero-mobile-light.svg?v=studio-20261021" />
  <source media="(prefers-color-scheme: dark)" srcset="./assets/profile-hero-dark.svg?v=studio-20261021" />
  <img width="100%" src="./assets/profile-hero-light.svg?v=studio-20261021" alt="Seung-Won Yu — Useful tools. Playful worlds. AI 도구와 게임 원화가 함께 놓인 작업실." />
</picture>

<p align="center">
  <a href="https://seung-won-yu.github.io/autolabel/">autolabel</a>
  &nbsp;&nbsp;
  <a href="https://github.com/Seung-Won-Yu/workroom-portal-public">Workroom Portal</a>
  &nbsp;&nbsp;
  <a href="https://seung-won-yu.github.io/pocket-desk-os/">PocketDesk OS</a>
  &nbsp;&nbsp;
  <a href="https://seung-won-yu.github.io/rune-drift-survivors/">Rune Drift Survivors</a>
</p>

AI 도구와 웹 제품, 그리고 **직접 플레이할 수 있는 게임**을 만듭니다.
아이디어를 **써볼 수 있는 것**으로 옮기고, 실제 동작까지 검증합니다.

## Selected work

### autolabel

**모델이 초안을 만들고, 사람은 예외를 고칩니다.**

<a href="https://seung-won-yu.github.io/autolabel/">
  <img width="100%" src="./assets/showcase/autolabel.svg?v=studio-20261021" alt="autolabel 미리보기 — 실제 PCB 결함 샘플의 모델 초안과 검수 화면" />
</a>

이미지 라벨링을 초안 생성 → 예외 검수 → 전용 모델 학습으로 연결한 로컬 AI 도구입니다.
기본 경로는 필수 API 키 없이 동작하며, COCO·YOLO 출력과 성능 재현 방법을 제공합니다.

<sub>Python · FastAPI · React · SQLite · 로컬 AI</sub>

**[소개와 실측 성능](https://seung-won-yu.github.io/autolabel/)** &nbsp; · &nbsp; [소스와 실행 방법](https://github.com/Seung-Won-Yu/autolabel)

<br />

### Workroom Portal

**개인의 AI 작업을 팀이 함께 쓰는 결과물로.**

<a href="https://github.com/Seung-Won-Yu/workroom-portal-public">
  <img width="100%" src="./assets/showcase/workroom-portal.svg?v=studio-20261021" alt="Workroom Portal 공개판 미리보기 — 팀 산출물과 보관함을 점검하는 관리자 대시보드" />
</a>

리서치·개발·요약 에이전트에 요청하고, 결과를 개인 작업공간에서 팀 공유로 이어가는 포털입니다.
스킬 라우팅, 비동기 작업 큐, 권한 경계와 감사 기록을 하나의 흐름으로 묶었습니다.

<sub>Python · React · TypeScript · 에이전트 운영 · 조직·구성원 정보를 예시 값으로 바꾼 공개판</sub>

**[소스와 실행 방법](https://github.com/Seung-Won-Yu/workroom-portal-public)** &nbsp; · &nbsp; [구조와 설계](https://github.com/Seung-Won-Yu/workroom-portal-public#구조)

<br />

### PocketDesk OS

**브라우저 탭 하나에 담은 작은 데스크톱.**

<a href="https://seung-won-yu.github.io/pocket-desk-os/">
  <img width="100%" src="./assets/showcase/pocket-desk-os.svg?v=studio-20261021" alt="PocketDesk OS 실제 화면 — 배경화면과 내 PC, 휴지통, 작업 표시줄이 있는 웹 데스크톱" />
</a>

창을 열고 옮기고, 가상 파일을 정리하고, 메모장·그림판·게임을 실행하는 웹 데스크톱입니다.
창과 파일 상태를 저장하고 PWA로 설치할 수 있습니다.

<sub>React · TypeScript · Vite · IndexedDB · PWA</sub>

**[데스크톱 열기](https://seung-won-yu.github.io/pocket-desk-os/)** &nbsp; · &nbsp; [소스와 검증 방법](https://github.com/Seung-Won-Yu/pocket-desk-os)

<br />

### Rune Drift Survivors · Ash &amp; Amber

**작은 숲에서 시작하는, 한 판 5분의 생존.**

<a href="https://seung-won-yu.github.io/rune-drift-survivors/">
  <img width="100%" src="./assets/showcase/rune-drift-survivors.svg?v=studio-20261021" alt="Rune Drift Survivors의 현재 챕터 Ash & Amber — 게임 원화와 실제 전투 화면" />
</a>

동료를 고르고, 자동 전투로 경험치를 모으고, 무기를 진화시켜 보스에 도전하는 2D 브라우저 로그라이트입니다.
키보드와 터치 조작을 지원하며, 동료·도감·전투 기록은 현재 브라우저에 저장됩니다.

<sub>Canvas 2D · JavaScript · Vite · 키보드·터치 · 설치 없이 플레이</sub>

**[게임 시작](https://seung-won-yu.github.io/rune-drift-survivors/)** &nbsp; · &nbsp; [소스와 플레이 가이드](https://github.com/Seung-Won-Yu/rune-drift-survivors)

<br />

## Tools & experiments

- **[Codex Agent Kit](https://seung-won-yu.github.io/codex-agent-kit/)** — 거친 요청을 명확한 실행과 검증으로 연결하는 개인 Codex 설정. [소스](https://github.com/Seung-Won-Yu/codex-agent-kit)
- **[blog-writing](https://github.com/Seung-Won-Yu/blog-writing)** — 후보 수집과 중복 제거를 거쳐 티스토리 발행용 초안을 만드는 파이프라인.

<details>
<summary>더 작은 실험들</summary>

- **[Apple Burst](https://seung-won-yu.github.io/apple-burst/)** — 합이 10이 되는 사과를 터뜨리는 캐주얼 게임. [소스](https://github.com/Seung-Won-Yu/apple-burst)
- **[PangPang Anipang](https://github.com/Seung-Won-Yu/pangpang-anipang)** — React + TypeScript 매치 게임 프로토타입.
- **[cart-ocr](https://github.com/Seung-Won-Yu/cart-ocr)** — 장바구니 영수증 OCR 실험.

</details>

## Behind the scenes

소스가 비공개인 작업은 공개 가능한 설계와 검증 관점으로 소개합니다.

- **edgelab** — 미국주식 4전략 모의투자 검증 랩. 판단 기록을 불변 저널로 남기고, 규칙이 바뀌면 평가 표본을 분리하는 구조를 만들었습니다.
- **AIVIS** — AI 산업안전 통합 관제. 보호구 착용·낙상 감지, 얼굴 식별, 실시간 대시보드를 하나의 관제 흐름으로 묶었습니다.

## How I work

**범위를 정하고 → 작게 만들고 → 실제로 확인하고 → 기록합니다.**

- **직접 확인합니다.** 화면은 브라우저에서 조작하고, 수치는 손계산과 대조합니다.
- **고친 것은 고정합니다.** 발견한 결함을 회귀 테스트와 CI에 남깁니다.
- **다른 시선으로 다시 봅니다.** 독립 감사에서 나온 발견을 코드와 대조해 반영합니다.

<details>
<summary>주로 쓰는 도구와 공개 원칙</summary>

Python · TypeScript · React · Vite · SQLite · Firebase · Supabase · GitHub Actions

사내 코드를 공개할 때는 조직·구성원 식별자를 제거하고, 커밋 직전 같은 검사를 다시 수행합니다.

</details>

---

<p align="center"><sub>Small ideas, thoughtfully shipped.</sub></p>
