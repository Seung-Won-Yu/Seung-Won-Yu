<p>
<picture>
  <source media="(prefers-color-scheme: dark) and (max-width: 1011px)" srcset="https://raw.githubusercontent.com/Seung-Won-Yu/Seung-Won-Yu/f72f361059fd7eca0e68e5de9abe734173304eec/assets/profile-hero-mobile-dark.svg" />
  <source media="(max-width: 1011px)" srcset="https://raw.githubusercontent.com/Seung-Won-Yu/Seung-Won-Yu/f72f361059fd7eca0e68e5de9abe734173304eec/assets/profile-hero-mobile-light.svg" />
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Seung-Won-Yu/Seung-Won-Yu/f72f361059fd7eca0e68e5de9abe734173304eec/assets/profile-hero-dark.svg" />
  <img width="100%" src="https://raw.githubusercontent.com/Seung-Won-Yu/Seung-Won-Yu/f72f361059fd7eca0e68e5de9abe734173304eec/assets/profile-hero-light.svg" alt="Seung-Won Yu. AI 도구·웹 제품·게임을 만들고 실제 동작과 검증 기록을 남깁니다. AI: 검수와 전용 모델 학습. Web: 상태 저장과 오프라인. Games: 5분 로그라이트. 네이비·블루와 앰버 포인트의 배너 프레임 밖으로 큰 Ash &amp; Amber 캐릭터가 나와 움직입니다." />
</picture>
</p>

[대표작](#selected-work) &nbsp;&nbsp; [만드는 방식](#approach) &nbsp;&nbsp; [더 살펴보기](#more-work) &nbsp;&nbsp; [이메일](mailto:a98857283@gmail.com)

## Selected work

### autolabel

<p>
<a href="https://seung-won-yu.github.io/autolabel/">
  <picture>
    <source media="(prefers-color-scheme: dark) and (max-width: 1011px)" srcset="https://raw.githubusercontent.com/Seung-Won-Yu/Seung-Won-Yu/0e70ee5da028e4e31479150b73477a1985ed3147/assets/features/autolabel-mobile-dark.svg" />
    <source media="(max-width: 1011px)" srcset="https://raw.githubusercontent.com/Seung-Won-Yu/Seung-Won-Yu/0e70ee5da028e4e31479150b73477a1985ed3147/assets/features/autolabel-mobile-light.svg" />
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Seung-Won-Yu/Seung-Won-Yu/0e70ee5da028e4e31479150b73477a1985ed3147/assets/features/autolabel-dark.svg" />
    <img width="100%" src="https://raw.githubusercontent.com/Seung-Won-Yu/Seung-Won-Yu/0e70ee5da028e4e31479150b73477a1985ed3147/assets/features/autolabel-light.svg" alt="autolabel 공개 검수 미리보기. PCB mAP50 0.963, 승인 300장·고정 홀드아웃·M4 Pro/MPS 자체 측정." />
  </picture>
</a>
</p>

모델이 만든 초안에서 **예외만 검수하고, 승인 데이터로 전용 모델을 학습**하는 로컬 AI 도구입니다.

**핵심 결과 — PCB mAP50 0.963.** 승인 300장, 고정 홀드아웃·M4 Pro/MPS 단일 머신의 자체 측정입니다. 후보 모델과 현재 모델을 같은 분할에서 비교합니다.

<sub>Python · FastAPI · React · SQLite</sub>

[제품 소개](https://seung-won-yu.github.io/autolabel/) &nbsp; · &nbsp; [소스](https://github.com/Seung-Won-Yu/autolabel) &nbsp; · &nbsp; [측정 조건과 재현 방법](https://github.com/Seung-Won-Yu/autolabel#얼마나-잘-되나)

<br />

### Workroom Portal

<p>
<a href="https://github.com/Seung-Won-Yu/workroom-portal-public">
  <picture>
    <source media="(prefers-color-scheme: dark) and (max-width: 1011px)" srcset="https://raw.githubusercontent.com/Seung-Won-Yu/Seung-Won-Yu/0e70ee5da028e4e31479150b73477a1985ed3147/assets/features/workroom-portal-mobile-dark.svg" />
    <source media="(max-width: 1011px)" srcset="https://raw.githubusercontent.com/Seung-Won-Yu/Seung-Won-Yu/0e70ee5da028e4e31479150b73477a1985ed3147/assets/features/workroom-portal-mobile-light.svg" />
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Seung-Won-Yu/Seung-Won-Yu/0e70ee5da028e4e31479150b73477a1985ed3147/assets/features/workroom-portal-dark.svg" />
    <img width="100%" src="https://raw.githubusercontent.com/Seung-Won-Yu/Seung-Won-Yu/0e70ee5da028e4e31479150b73477a1985ed3147/assets/features/workroom-portal-light.svg" alt="Workroom Portal 공개판 관리자 대시보드. 명시적 공유와 개인·팀·관리자 접근 경계, 권한·경로·스트리밍 회귀 점검." />
  </picture>
</a>
</p>

리서치·개발·요약 에이전트의 결과를 **개인 작업공간에서 팀 공유와 관리자 점검으로 연결**하는 포털입니다.

**핵심 구현 — 개인·공유·관리자 접근 범위 분리.** 명시적으로 공유한 결과만 팀으로 넘기고, 권한 밖 접근은 사유를 기록합니다. 권한·경로·스트리밍 회귀를 자체 점검에 묶었습니다.

<sub>Python · React · TypeScript · 공개판의 조직·구성원 식별자는 예시 값</sub>

[공개판과 실행 방법](https://github.com/Seung-Won-Yu/workroom-portal-public) &nbsp; · &nbsp; [권한 경계와 설계](https://github.com/Seung-Won-Yu/workroom-portal-public#권한-경계) &nbsp; · &nbsp; [점검 방법](https://github.com/Seung-Won-Yu/workroom-portal-public#실행)

<br />

### PocketDesk OS

<p>
<a href="https://seung-won-yu.github.io/pocket-desk-os/">
  <picture>
    <source media="(prefers-color-scheme: dark) and (max-width: 1011px)" srcset="https://raw.githubusercontent.com/Seung-Won-Yu/Seung-Won-Yu/0e70ee5da028e4e31479150b73477a1985ed3147/assets/features/pocket-desk-os-mobile-dark.svg" />
    <source media="(max-width: 1011px)" srcset="https://raw.githubusercontent.com/Seung-Won-Yu/Seung-Won-Yu/0e70ee5da028e4e31479150b73477a1985ed3147/assets/features/pocket-desk-os-mobile-light.svg" />
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Seung-Won-Yu/Seung-Won-Yu/0e70ee5da028e4e31479150b73477a1985ed3147/assets/features/pocket-desk-os-dark.svg" />
    <img width="100%" src="https://raw.githubusercontent.com/Seung-Won-Yu/Seung-Won-Yu/0e70ee5da028e4e31479150b73477a1985ed3147/assets/features/pocket-desk-os-light.svg" alt="PocketDesk OS 실행 화면. 17개 앱과 9단계 QA 게이트, 브라우저·접근성·오프라인 확인." />
  </picture>
</a>
</p>

창을 옮기고 파일을 정리하며 앱을 실행하는 **브라우저 안의 데스크톱**입니다. 창·아이콘·테마·가상 파일을 IndexedDB에 보존하고 PWA로 설치할 수 있습니다.

**검증 범위 — 17개 앱 · 9단계 QA 게이트.** 파일·ZIP, 실제 브라우저 흐름, ARIA·포커스, 서비스워커의 오프라인 재실행을 하나의 확인 경로로 묶었습니다.

<sub>React · TypeScript · Vite · IndexedDB · PWA</sub>

[데스크톱 열기](https://seung-won-yu.github.io/pocket-desk-os/) &nbsp; · &nbsp; [소스](https://github.com/Seung-Won-Yu/pocket-desk-os) &nbsp; · &nbsp; [QA 게이트](https://github.com/Seung-Won-Yu/pocket-desk-os#품질-확인)

<br />

### Rune Drift Survivors · Ash &amp; Amber

<p>
<a href="https://seung-won-yu.github.io/rune-drift-survivors/">
  <picture>
    <source media="(prefers-color-scheme: dark) and (max-width: 1011px)" srcset="https://raw.githubusercontent.com/Seung-Won-Yu/Seung-Won-Yu/0e70ee5da028e4e31479150b73477a1985ed3147/assets/features/rune-drift-survivors-mobile-dark.svg" />
    <source media="(max-width: 1011px)" srcset="https://raw.githubusercontent.com/Seung-Won-Yu/Seung-Won-Yu/0e70ee5da028e4e31479150b73477a1985ed3147/assets/features/rune-drift-survivors-mobile-light.svg" />
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Seung-Won-Yu/Seung-Won-Yu/0e70ee5da028e4e31479150b73477a1985ed3147/assets/features/rune-drift-survivors-dark.svg" />
    <img width="100%" src="https://raw.githubusercontent.com/Seung-Won-Yu/Seung-Won-Yu/0e70ee5da028e4e31479150b73477a1985ed3147/assets/features/rune-drift-survivors-light.svg" alt="Ash & Amber 실제 전투 화면. 전투 모멘텀 패스 unit 75개·browser 20개 검증. 데스크톱 브라우저 3개 viewport 범위." />
  </picture>
</a>
</p>

동료를 고르고 무기를 진화시켜 숲의 보스에 도전하는 **한 판 5분의 2D 브라우저 로그라이트**입니다. 키보드·터치를 지원하고, 전투 연출을 실제 타격·이동 시계에 연결했습니다.

**검증 기록 — unit 75개 · browser 20개.** 전투 모멘텀 패스의 데스크톱 브라우저 3개 viewport에서 p95 프레임 간격 16.7–16.8ms를 기록했습니다. 물리 휴대폰의 성능 측정은 아닙니다.

<sub>Canvas 2D · JavaScript · Vite</sub>

[게임 시작](https://seung-won-yu.github.io/rune-drift-survivors/) &nbsp; · &nbsp; [소스](https://github.com/Seung-Won-Yu/rune-drift-survivors) &nbsp; · &nbsp; [전투·프레임 검증 기록](https://github.com/Seung-Won-Yu/rune-drift-survivors/blob/main/docs/design/survivor-restart/42-COMBAT-MOMENTUM.md#L12-L16)

<br />

## Approach

<p>
<picture>
  <source media="(prefers-color-scheme: dark) and (max-width: 1011px)" srcset="https://raw.githubusercontent.com/Seung-Won-Yu/Seung-Won-Yu/0e70ee5da028e4e31479150b73477a1985ed3147/assets/sections/approach-mobile-dark.svg" />
  <source media="(max-width: 1011px)" srcset="https://raw.githubusercontent.com/Seung-Won-Yu/Seung-Won-Yu/0e70ee5da028e4e31479150b73477a1985ed3147/assets/sections/approach-mobile-light.svg" />
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Seung-Won-Yu/Seung-Won-Yu/0e70ee5da028e4e31479150b73477a1985ed3147/assets/sections/approach-dark.svg" />
  <img width="100%" src="https://raw.githubusercontent.com/Seung-Won-Yu/Seung-Won-Yu/0e70ee5da028e4e31479150b73477a1985ed3147/assets/sections/approach-light.svg" alt="만드는 방식. 흐름을 먼저 봅니다: 입력에서 결과까지 이어지는 경로와 사람이 판단해야 하는 지점을 정리합니다. 실제로 사용해 봅니다: 저장·복원·실패·오프라인 경로도 브라우저에서 확인합니다. 고친 것은 기록합니다: 발견한 결함을 회귀 테스트와 CI에 남기고 측정 조건과 한계를 기록합니다." />
</picture>
</p>

## More work

<p>
<a href="https://seung-won-yu.github.io/codex-agent-kit/">
<picture>
  <source media="(prefers-color-scheme: dark) and (max-width: 1011px)" srcset="https://raw.githubusercontent.com/Seung-Won-Yu/Seung-Won-Yu/0e70ee5da028e4e31479150b73477a1985ed3147/assets/sections/codex-agent-kit-mobile-dark.svg" />
  <source media="(max-width: 1011px)" srcset="https://raw.githubusercontent.com/Seung-Won-Yu/Seung-Won-Yu/0e70ee5da028e4e31479150b73477a1985ed3147/assets/sections/codex-agent-kit-mobile-light.svg" />
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Seung-Won-Yu/Seung-Won-Yu/0e70ee5da028e4e31479150b73477a1985ed3147/assets/sections/codex-agent-kit-dark.svg" />
  <img width="100%" src="https://raw.githubusercontent.com/Seung-Won-Yu/Seung-Won-Yu/0e70ee5da028e4e31479150b73477a1985ed3147/assets/sections/codex-agent-kit-light.svg" alt="Codex Agent Kit — 요청의 의도를 실행·검증까지 연결하는 개인 Codex 설정과 스킬 구성." />
</picture>
</a>
</p>

[가이드 열기](https://seung-won-yu.github.io/codex-agent-kit/) &nbsp; · &nbsp; [소스](https://github.com/Seung-Won-Yu/codex-agent-kit)

<p>
<a href="https://github.com/Seung-Won-Yu/blog-writing">
<picture>
  <source media="(prefers-color-scheme: dark) and (max-width: 1011px)" srcset="https://raw.githubusercontent.com/Seung-Won-Yu/Seung-Won-Yu/0e70ee5da028e4e31479150b73477a1985ed3147/assets/sections/blog-writing-mobile-dark.svg" />
  <source media="(max-width: 1011px)" srcset="https://raw.githubusercontent.com/Seung-Won-Yu/Seung-Won-Yu/0e70ee5da028e4e31479150b73477a1985ed3147/assets/sections/blog-writing-mobile-light.svg" />
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Seung-Won-Yu/Seung-Won-Yu/0e70ee5da028e4e31479150b73477a1985ed3147/assets/sections/blog-writing-dark.svg" />
  <img width="100%" src="https://raw.githubusercontent.com/Seung-Won-Yu/Seung-Won-Yu/0e70ee5da028e4e31479150b73477a1985ed3147/assets/sections/blog-writing-light.svg" alt="blog-writing — 후보 수집과 중복 제거를 거쳐 티스토리 발행용 초안을 만드는 파이프라인." />
</picture>
</a>
</p>

[저장소 보기](https://github.com/Seung-Won-Yu/blog-writing)

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
