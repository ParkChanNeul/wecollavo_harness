---
name: wecollavo-interview-intake
description: Start a WeCollavo interview in intake-first mode without reading or writing any client workspace.
---

# WeCollavo Interview Intake

Use this skill for bare `$wecollavo-interview`, legacy bare start command, or
any interview start request without an explicit workspace.

## Read First

- `docs/source-of-truth.md`
- `docs/language-contract.md`
- `docs/wecollavo-interview.md`
- `docs/department-analysis-method.md`
- `docs/security.md`

## Role

Start the meeting conversation by collecting customer context before any client
workspace is read.

## Inputs

- No required files.
- Optional customer/company name.
- Optional raw customer utterance typed by Channeul.
- Optional service interest or meeting purpose.

## Output

Return:

```text
# WeCollavo Interview Intake

## Before We Start
아직 client workspace를 읽지 않았습니다.
고객 정보를 먼저 입력해 주세요.

## Intake Questions
1. 신규 고객인가요, 기존 고객인가요?
2. 고객/회사명은 무엇인가요?
3. 오늘 미팅 목적은 무엇인가요?
4. 고객이 처음 한 말 또는 문의 내용은 무엇인가요?
5. 관심 서비스는 무엇인가요?
   - 홈페이지 / 랜딩페이지 / 로고 / 브로셔 / 회사소개서 / 브랜드 키트 / 콘텐츠 / 마케팅 운영 / 기타
6. 예산, 일정, 자료 상태 중 이미 알고 있는 것이 있나요?
7. 기존 client workspace에 연결할까요, 아니면 임시 인터뷰로 진행할까요?

## Next Action
고객 발화를 받으면 `$wecollavo-interview-turn`으로 AI Interview Card를 생성합니다.
기존 워크스페이스를 사용하려면 `client_dir=clients/<client>`를 명시해 주세요.
```

## Forbidden

- Do not read `clients/<client>` files.
- Do not infer active client from recent work, customer name, or repo contents.
- Do not treat `clients/gt-engineering` as active unless explicitly named.
- Do not write, update, or lock `meeting-state.md`.
- Do not create `proposal-data.json`.

## Non-linear Entry

This skill can always start. It does not require prior state and must not read,
write, update, or lock client workspace files.

## Next Skill Handoff

- Recommended Next Skill: `$wecollavo-interview-turn`
- Why: Use when Channeul provides the first customer utterance.
- Ready To Continue: yes | no
- Need Channeul Confirmation: yes
- Requires client_dir: no
- Suggested Prompt: `$wecollavo-interview-turn 고객 발화: <고객이 말한 내용>`

If the user explicitly names a workspace path or existing client id, recommend
`$wecollavo-workspace-resume` instead. This handoff is a recommendation only.
