<picture>
  <source media="(prefers-color-scheme: dark) and (max-width: 600px)" srcset="https://raw.githubusercontent.com/Seung-Won-Yu/Seung-Won-Yu/1b8b86ebb4e8ccde181697d5014af143fb9946d3/assets/profile-hero-mobile-dark.svg" />
  <source media="(max-width: 600px)" srcset="https://raw.githubusercontent.com/Seung-Won-Yu/Seung-Won-Yu/1b8b86ebb4e8ccde181697d5014af143fb9946d3/assets/profile-hero-mobile-light.svg" />
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Seung-Won-Yu/Seung-Won-Yu/1b8b86ebb4e8ccde181697d5014af143fb9946d3/assets/profile-hero-dark.svg" />
  <img width="100%" src="https://raw.githubusercontent.com/Seung-Won-Yu/Seung-Won-Yu/1b8b86ebb4e8ccde181697d5014af143fb9946d3/assets/profile-hero-light.svg" alt="Seung-Won Yu — AI 도구, 웹 제품, 브라우저 게임을 만듭니다. 작은 Ash & Amber 캐릭터가 걷는 동작을 보여줍니다." />
</picture>

AI 워크플로부터 웹 인터페이스와 게임까지, **직접 써볼 수 있는 제품과 검증 기록**을 만듭니다.

[대표작](#selected-work) &nbsp;&nbsp; [만드는 방식](#approach) &nbsp;&nbsp; [더 살펴보기](#more-work) &nbsp;&nbsp; [이메일](mailto:a98857283@gmail.com)

## Selected work

<p>
  <img align="left" width="96" src="https://raw.githubusercontent.com/Seung-Won-Yu/Seung-Won-Yu/1b8b86ebb4e8ccde181697d5014af143fb9946d3/assets/showcase/autolabel.svg" alt="" />
  <strong><a href="#autolabel">autolabel</a></strong><br />
  <strong>PCB mAP50 0.963</strong><br />
  <sub>승인 300장·홀드아웃·자체측정</sub>
</p>
<br clear="left" />

<p>
  <img align="left" width="96" src="https://raw.githubusercontent.com/Seung-Won-Yu/Seung-Won-Yu/1b8b86ebb4e8ccde181697d5014af143fb9946d3/assets/showcase/workroom-portal.svg" alt="" />
  <strong><a href="#workroom-portal">Workroom Portal</a></strong><br />
  <strong>개인·공유·관리자 경계</strong><br />
  <sub>권한·경로·스트리밍 회귀</sub>
</p>
<br clear="left" />

<p>
  <img align="left" width="96" src="https://raw.githubusercontent.com/Seung-Won-Yu/Seung-Won-Yu/1b8b86ebb4e8ccde181697d5014af143fb9946d3/assets/showcase/pocket-desk-os.svg" alt="" />
  <strong><a href="#pocketdesk-os">PocketDesk OS</a></strong><br />
  <strong>17개 앱 · 9단계 QA</strong><br />
  <sub>브라우저·접근성·오프라인</sub>
</p>
<br clear="left" />

<p>
  <img align="left" width="96" src="https://raw.githubusercontent.com/Seung-Won-Yu/Seung-Won-Yu/1b8b86ebb4e8ccde181697d5014af143fb9946d3/assets/showcase/rune-drift-survivors.svg" alt="" />
  <strong><a href="#rune-drift-survivors--ash--amber">Rune Drift Survivors</a></strong><br />
  <strong>75 unit · 20 browser 검증</strong><br />
  <sub>전투 패스·데스크톱 브라우저</sub>
</p>
<br clear="left" />

### autolabel

모델이 만든 초안에서 **예외만 검수하고, 승인 데이터로 전용 모델을 학습**하는 로컬 AI 도구입니다.

**핵심 결과 — PCB mAP50 0.963.** 승인 300장, 고정 홀드아웃·M4 Pro/MPS 단일 머신의 자체 측정입니다. 후보 모델과 현재 모델을 같은 분할에서 비교합니다.

<a href="https://seung-won-yu.github.io/autolabel/">
  <img width="640" src="https://raw.githubusercontent.com/Seung-Won-Yu/Seung-Won-Yu/1b8b86ebb4e8ccde181697d5014af143fb9946d3/assets/showcase/autolabel.svg" alt="autolabel 공개 검수 미리보기 — 모델 초안, PCB 결함 샘플, 검수할 어노테이션" />
</a>

<sub>Python · FastAPI · React · SQLite</sub>

[제품 소개](https://seung-won-yu.github.io/autolabel/) &nbsp; · &nbsp; [소스](https://github.com/Seung-Won-Yu/autolabel) &nbsp; · &nbsp; [측정 조건과 재현 방법](https://github.com/Seung-Won-Yu/autolabel#얼마나-잘-되나)

<br />

### Workroom Portal

리서치·개발·요약 에이전트의 결과를 **개인 작업공간에서 팀 공유와 관리자 점검으로 연결**하는 포털입니다.

**핵심 구현 — 개인·공유·관리자 접근 범위 분리.** 명시적으로 공유한 결과만 팀으로 넘기고, 권한 밖 접근은 사유를 기록합니다. 권한·경로·스트리밍 회귀를 자체 점검에 묶었습니다.

<a href="https://github.com/Seung-Won-Yu/workroom-portal-public">
  <img width="640" src="https://raw.githubusercontent.com/Seung-Won-Yu/Seung-Won-Yu/1b8b86ebb4e8ccde181697d5014af143fb9946d3/assets/showcase/workroom-portal.svg" alt="Workroom Portal 공개판의 관리자 대시보드" />
</a>

<sub>Python · React · TypeScript · 공개판의 조직·구성원 식별자는 예시 값</sub>

[공개판과 실행 방법](https://github.com/Seung-Won-Yu/workroom-portal-public) &nbsp; · &nbsp; [권한 경계와 설계](https://github.com/Seung-Won-Yu/workroom-portal-public#권한-경계) &nbsp; · &nbsp; [점검 방법](https://github.com/Seung-Won-Yu/workroom-portal-public#실행)

<br />

### PocketDesk OS

창을 옮기고 파일을 정리하며 앱을 실행하는 **브라우저 안의 데스크톱**입니다. 창·아이콘·테마·가상 파일을 IndexedDB에 보존하고 PWA로 설치할 수 있습니다.

**검증 범위 — 17개 앱 · 9단계 QA 게이트.** 파일·ZIP, 실제 브라우저 흐름, ARIA·포커스, 서비스워커의 오프라인 재실행을 하나의 확인 경로로 묶었습니다.

<a href="https://seung-won-yu.github.io/pocket-desk-os/">
  <img width="640" src="https://raw.githubusercontent.com/Seung-Won-Yu/Seung-Won-Yu/1b8b86ebb4e8ccde181697d5014af143fb9946d3/assets/showcase/pocket-desk-os.svg" alt="PocketDesk OS — 창, 파일, 기본 앱과 작업 표시줄이 있는 데스크톱 화면" />
</a>

<sub>React · TypeScript · Vite · IndexedDB · PWA</sub>

[데스크톱 열기](https://seung-won-yu.github.io/pocket-desk-os/) &nbsp; · &nbsp; [소스](https://github.com/Seung-Won-Yu/pocket-desk-os) &nbsp; · &nbsp; [QA 게이트](https://github.com/Seung-Won-Yu/pocket-desk-os#품질-확인)

<br />

### Rune Drift Survivors · Ash &amp; Amber

동료를 고르고 무기를 진화시켜 숲의 보스에 도전하는 **한 판 5분의 2D 브라우저 로그라이트**입니다. 키보드·터치를 지원하고, 전투 연출을 실제 타격·이동 시계에 연결했습니다.

**검증 기록 — unit 75개 · browser 20개.** 전투 모멘텀 패스의 데스크톱 브라우저 3개 viewport에서 p95 프레임 간격 16.7–16.8ms를 기록했습니다. 물리 휴대폰의 성능 측정은 아닙니다.

<a href="https://seung-won-yu.github.io/rune-drift-survivors/">
  <img width="640" src="https://raw.githubusercontent.com/Seung-Won-Yu/Seung-Won-Yu/1b8b86ebb4e8ccde181697d5014af143fb9946d3/assets/showcase/rune-drift-survivors.svg" alt="Ash & Amber의 실제 전투 화면 — 플레이어, 적과 전투 HUD" />
</a>

<sub>Canvas 2D · JavaScript · Vite</sub>

[게임 시작](https://seung-won-yu.github.io/rune-drift-survivors/) &nbsp; · &nbsp; [소스](https://github.com/Seung-Won-Yu/rune-drift-survivors) &nbsp; · &nbsp; [전투·프레임 검증 기록](https://github.com/Seung-Won-Yu/rune-drift-survivors/blob/main/docs/design/survivor-restart/42-COMBAT-MOMENTUM.md#L12-L16)

<br />

## Approach

- **흐름을 먼저 봅니다.** 입력에서 결과까지 이어지는 경로와 사람이 판단해야 하는 지점을 정리합니다.
- **실제로 사용해 봅니다.** 저장·복원·실패·오프라인처럼 놓치기 쉬운 경로도 브라우저에서 확인합니다.
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

[Email](mailto:a98857283@gmail.com) &nbsp; · &nbsp; [Repositories](https://github.com/Seung-Won-Yu?tab=repositories)
