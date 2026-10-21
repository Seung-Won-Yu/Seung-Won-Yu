<picture>
  <source media="(prefers-color-scheme: dark) and (max-width: 600px)" srcset="./assets/profile-hero-mobile-dark.svg?v=portfolio-20261021" />
  <source media="(max-width: 600px)" srcset="./assets/profile-hero-mobile-light.svg?v=portfolio-20261021" />
  <source media="(prefers-color-scheme: dark)" srcset="./assets/profile-hero-dark.svg?v=portfolio-20261021" />
  <img width="100%" src="./assets/profile-hero-light.svg?v=portfolio-20261021" alt="Seung-Won Yu — 유승원. AI 도구와 웹 제품, 플레이할 수 있는 세계를 만듭니다. Ash & Amber의 캐릭터가 실제 걷기 동작을 보여줍니다." />
</picture>

<p align="center">
  <a href="#selected-work">대표작</a> &nbsp;&nbsp; / &nbsp;&nbsp;
  <a href="#approach">만드는 방식</a> &nbsp;&nbsp; / &nbsp;&nbsp;
  <a href="#more-work">더 살펴보기</a> &nbsp;&nbsp; / &nbsp;&nbsp;
  <a href="mailto:a98857283@gmail.com">이메일</a>
</p>

반복 작업을 줄이는 **AI 도구**와, 브라우저에서 직접 경험할 수 있는 **웹 제품과 게임**을 만듭니다.
화면뿐 아니라 그 뒤의 워크플로, 상태, 검증까지 함께 다룹니다.

## Selected work

### autolabel

**검수할 것만 남기는 라벨링 워크플로.**

<a href="https://seung-won-yu.github.io/autolabel/">
  <img width="100%" src="./assets/showcase/autolabel.svg?v=portfolio-20261021" alt="autolabel — 실제 PCB 결함 샘플과 모델 초안·검수 화면. 입력에서 예외 검수와 전용 모델 학습으로 이어지는 흐름." />
</a>

전수 수동 라벨링을 **모델 초안 → 예외 검수 → 전용 모델 학습**의 반복으로 바꾼 로컬 AI 도구입니다. 기본 경로는 필수 API 키 없이 동작하며 COCO·YOLO로 결과를 내보냅니다.

- **설계 판단** — 승인한 이미지만 학습에 쓰고, 같은 검증 분할에서 후보 모델과 현재 모델을 비교합니다. 결과에는 모델·프롬프트·임계값의 출처를 남깁니다.
- **검증 근거** — 고정 홀드아웃의 PCB 결함 실험에서 승인 300장으로 **mAP50 0.963**을 기록했습니다. M4 Pro/MPS 단일 머신의 자체 측정이며, [조건과 재현 방법](https://github.com/Seung-Won-Yu/autolabel#얼마나-잘-되나)을 공개합니다.

<sub>Python · FastAPI · React · SQLite</sub>

**[제품 소개와 실측 성능](https://seung-won-yu.github.io/autolabel/)** &nbsp; · &nbsp; [소스와 실행 방법](https://github.com/Seung-Won-Yu/autolabel)

<br />

### Workroom Portal

**개인의 AI 작업이 팀의 자산으로 이어지도록.**

<a href="https://github.com/Seung-Won-Yu/workroom-portal-public">
  <img width="100%" src="./assets/showcase/workroom-portal.svg?v=portfolio-20261021" alt="Workroom Portal 공개판의 실제 관리자 대시보드. 개인 작업, 팀 공유, 관리자 점검으로 이어지는 흐름." />
</a>

리서치·개발·요약 에이전트에 요청하고, 결과를 **개인 작업공간 → 팀 공유 → 관리자 점검**으로 연결하는 포털입니다.

- **설계 판단** — 요청에 맞춘 스킬 라우팅과 비동기 작업 큐를 묶고, 파일 접근의 스코프 판정을 한 모듈에 모았습니다. 권한 밖 접근은 사유와 함께 기록합니다.
- **검증 근거** — 권한·경로·스트리밍 회귀를 [자체 점검 절차](https://github.com/Seung-Won-Yu/workroom-portal-public#실행)에 고정했습니다. 공개판의 조직·구성원 식별자는 예시 값으로 치환했습니다.

<sub>Python · React · TypeScript · 에이전트 운영</sub>

**[공개판과 실행 방법](https://github.com/Seung-Won-Yu/workroom-portal-public)** &nbsp; · &nbsp; [구조와 설계](https://github.com/Seung-Won-Yu/workroom-portal-public#구조)

<br />

### PocketDesk OS

**닫았다 열어도, 작업이 남아 있는 데스크톱.**

<a href="https://seung-won-yu.github.io/pocket-desk-os/">
  <img width="100%" src="./assets/showcase/pocket-desk-os.svg?v=portfolio-20261021" alt="PocketDesk OS 실제 화면. 창·파일·기본 앱과 작업 표시줄을 갖춘 브라우저 데스크톱." />
</a>

창을 열고 옮기고, 파일을 정리하고, 메모장·그림판·게임을 실행하는 **브라우저 안의 작은 OS**입니다.

- **설계 판단** — 창·아이콘·테마·가상 파일을 IndexedDB에 보존하고, PWA로 설치할 수 있게 했습니다. 화면의 모양과 실제 작업 상태를 함께 다룹니다.
- **검증 근거** — 파일·ZIP 단위 테스트, 실제 브라우저 흐름, 17개 앱의 ARIA·포커스, 서비스워커의 오프라인 재실행을 [9단계 QA 게이트](https://github.com/Seung-Won-Yu/pocket-desk-os#품질-확인)에 묶었습니다.

<sub>React · TypeScript · Vite · IndexedDB · PWA</sub>

**[데스크톱 열기](https://seung-won-yu.github.io/pocket-desk-os/)** &nbsp; · &nbsp; [소스와 검증 방법](https://github.com/Seung-Won-Yu/pocket-desk-os)

<br />

### Rune Drift Survivors · Ash &amp; Amber

**짧은 한 판 안에, 선택과 성장의 손맛을.**

<a href="https://seung-won-yu.github.io/rune-drift-survivors/">
  <img width="100%" src="./assets/showcase/rune-drift-survivors.svg?v=portfolio-20261021" alt="Ash & Amber — 게임 원화와 실제 전투 화면. 동료 선택, 무기 진화, 보스전으로 이어지는 5분 생존 챕터." />
</a>

동료를 고르고, 자동 전투로 경험치를 모으고, 무기를 진화시켜 숲의 보스에 도전하는 **한 판 5분의 2D 브라우저 로그라이트**입니다. 키보드와 터치를 지원합니다.

- **설계 판단** — 전투 연출을 실제 타격·이동·시뮬레이션 시계에 연결했습니다. 동작 줄이기를 별도 처리해 연출이 판정이나 밸런스를 바꾸지 않게 했습니다.
- **검증 근거** — [전투 모멘텀 검증 기록](https://github.com/Seung-Won-Yu/rune-drift-survivors/blob/main/docs/design/survivor-restart/42-COMBAT-MOMENTUM.md)에 unit 75개·browser 20개와 세 화면 크기의 프레임 측정을 남겼습니다. 측정 환경은 데스크톱 브라우저입니다.

<sub>Canvas 2D · JavaScript · Vite · 설치 없이 플레이</sub>

**[게임 시작](https://seung-won-yu.github.io/rune-drift-survivors/)** &nbsp; · &nbsp; [소스와 플레이 가이드](https://github.com/Seung-Won-Yu/rune-drift-survivors)

<br />

## Approach

**작동하는 화면에서 끝내지 않고, 다시 확인할 수 있는 근거를 남깁니다.**

- **흐름을 먼저 봅니다.** 입력에서 결과까지 이어지는 경로와, 사람이 판단해야 하는 지점을 정리합니다.
- **실제로 사용해 봅니다.** 브라우저에서 화면을 조작하고, 저장·복원·실패·오프라인처럼 놓치기 쉬운 경로도 확인합니다.
- **고친 것은 기록합니다.** 발견한 결함은 회귀 테스트와 CI에 남기고, 측정 조건과 한계도 함께 적습니다.

## More work

- **[Codex Agent Kit](https://seung-won-yu.github.io/codex-agent-kit/)** — 요청의 의도를 실행·검증까지 연결하는 개인 Codex 설정과 스킬 구성. [소스](https://github.com/Seung-Won-Yu/codex-agent-kit)
- **[blog-writing](https://github.com/Seung-Won-Yu/blog-writing)** — 후보 수집과 중복 제거를 거쳐 티스토리 발행용 초안을 만드는 파이프라인.

<details>
<summary>비공개 작업에서 다룬 문제</summary>

소스 대신 공개 가능한 설계 관점을 소개합니다.

- **edgelab** — 미국주식 4전략 모의투자 검증 랩. 판단 기록을 불변 저널로 남기고, 규칙이 바뀌면 평가 표본을 분리하는 구조.
- **AIVIS** — AI 산업안전 통합 관제. 보호구 착용·낙상 감지, 얼굴 식별과 실시간 대시보드를 연결한 관제 흐름.

</details>

<details>
<summary>더 작은 실험들</summary>

- **[Apple Burst](https://seung-won-yu.github.io/apple-burst/)** — 합이 10이 되는 사과를 터뜨리는 캐주얼 게임. [소스](https://github.com/Seung-Won-Yu/apple-burst)
- **[PangPang Anipang](https://github.com/Seung-Won-Yu/pangpang-anipang)** — React + TypeScript 매치 게임 프로토타입.
- **[cart-ocr](https://github.com/Seung-Won-Yu/cart-ocr)** — 장바구니 영수증 OCR 실험.

</details>

---

**Seung-Won Yu · 유승원** &nbsp; [Email](mailto:a98857283@gmail.com) &nbsp; · &nbsp; [Repositories](https://github.com/Seung-Won-Yu?tab=repositories)
