# Motion Policy

Status: v1 future output adapter policy

v1 기본 고객 산출물은 static `proposal.html`이다. HyperFrames, GSAP, Lottie
같은 모션 출력은 v1.5 이후 선택 output adapter로만 다룬다.

## Current Output

- v1 출력은 `proposal.html` 하나다.
- `proposal-data.json`은 단일 제안 데이터 소스로 유지한다.
- `render_proposal.py`는 v1에서 HTML만 생성한다.
- HyperFrames 전용 폴더, `motion.json`, `lottie-manifest.json`은 v1에서
  만들지 않는다.

## Future Adapter

HyperFrames는 새 데이터 흐름이 아니라 렌더 타깃이다.

```text
proposal-data.json
  -> render target: html
  -> future render target: hyperframes
```

향후 확장 시에도 가격, 범위, 결제, 수정 조건은 같은 `proposal-data.json`에서
읽어야 한다. 모션 산출물을 위해 별도 가격 데이터나 별도 제안 데이터를 만들지
않는다.

## Motion Boundary

모션은 이해를 돕는 보조 표현이다. 아래 영역은 정적 가독성을 우선한다.

- 가격 분해표
- 결제 조건
- 수정/피드백 기준
- 추가비 발생 조건
- 최종 견적 안내
- Human Review 이후 확정되는 납품 약속

모션을 적용할 수 있는 영역은 아래로 제한한다.

- 커버
- 오늘의 결론
- 왜 이런 결론이 나왔는가
- 고객 상황 진단
- 30일 실행 계획
- 본 제작 제안

