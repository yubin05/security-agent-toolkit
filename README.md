# security-agent-toolkit

Python으로 보안 로그를 분석하고, LLM을 활용해 이벤트 요약과 보고서 생성을 자동화하는 학습 프로젝트입니다. SKT-ALEPH 1과목에서 진행한 2026년 9월 22일~10월 8일 실습 코드, 노트북, 학습 기록을 정리했습니다.

**[실행 가이드 및 수업 노트북](agent_core/README.md)** · **[보고서 예시](agent_core/daily_report_20261008.md)** · **[코드 리뷰·테스트·회고](docs/day08_retrospective.md)**

## 프로젝트 목표

- 로그의 구조를 이해하고 Python으로 정규화·집계·탐지 규칙을 구현하기
- API, 웹훅, 스케줄러와 LLM 호출을 단계적으로 연결하기
- 보안 이벤트를 위험도별로 정리하고 사람이 검토할 보고서를 생성하기
- 코드 리뷰와 테스트로 오류를 찾고 개선 방향을 기록하기

## 주요 기능

| 영역 | 구현 및 실습 내용 |
|---|---|
| 로그 처리 | 파일·CSV·JSON 처리, 정규식 탐지, 예외 처리와 로깅 |
| 외부 연동 | requests 기반 API 클라이언트, Flask 웹훅, 주기 실행 실습 |
| LLM 활용 | 프롬프트 구성, JSON 응답 파싱, 도구 선택·실행 실습 |
| 보고서 자동화 | 이벤트 배치 요약, 위험도 정렬, 전체 개요와 Markdown 보고서 생성 |
| 설정과 알림 | 모델·확인 기준·웹훅 설정 분리, 사람 확인 대상 집계와 알림 |
| 검증 | 함수별 assert 테스트 9건, 오류 상황 실행 확인, 논리 오류 디버깅 |

각 영역은 단계별 실습으로 구성되어 있습니다. 현재 통합 실행 대상은 다음 보고서 파이프라인이며, 이전 로그 탐지 스케줄러와 도구 실행 실습은 별도로 구성되어 있습니다.

```text
보안 이벤트 JSON
      ↓
LLM 이벤트 요약 → 위험도 정렬 → 전체 개요 생성
      ↓
Markdown 보고서 저장 → 사람 확인 대상 집계 → 웹훅 알림
```

## 저장소 구조

```text
security-agent-toolkit/
├── agent_core/
│   ├── README.md             # 실행 가이드·모듈 설명·수업 노트북 목록
│   ├── *.ipynb              # 날짜별 실습과 실행 기록
│   ├── pipeline.py          # 보고서 파이프라인 진입점
│   ├── llm_client.py        # LLM 호출·JSON 파싱
│   ├── event_summarizer.py  # 이벤트 요약·정렬
│   ├── report_generator.py  # 보고서 생성·저장
│   ├── notifier.py          # 확인 대상 판정·웹훅 전송
│   ├── alert_server.py      # 로컬 웹훅 수신 서버
│   ├── config.json          # 실행 설정
│   └── test_agent_core.py   # 함수 테스트
├── docs/                    # 날짜별 학습 기록·1과목 회고
└── README.md
```

## 실행 안내

Python, Gemini API 키, `requests`·`flask`가 필요합니다. 이전 스케줄러 실습에는 `schedule`도 사용합니다.

1. 가상환경과 의존성을 준비합니다.
2. 저장소 최상위 `.env`에 `GEMINI_API_KEY`를 설정합니다.
3. `agent_core` 폴더에서 `alert_server.py`를 실행합니다.
4. 별도 터미널의 같은 폴더에서 `pipeline.py`를 실행합니다.

명령어와 설정별 동작은 **[agent_core 실행 가이드](agent_core/README.md#실행-방법)**에 정리했습니다. API 키는 저장소에 포함하지 않습니다.

현재 입력은 `events_1008.json`으로 고정되어 있으며, 출력은 실행 날짜에 따른 `daily_report_YYYYMMDD.md`입니다. `report_folder` 설정은 실제 저장 경로에 아직 반영되어 있지 않습니다. 사람 확인 대상은 건수로 알리며, 승인 대기 절차는 구현하지 않았습니다.

## 코드 리뷰와 테스트

보고서 한 줄 형식, 확인 기준 판정, LLM JSON 파싱을 대상으로 **assert 9건**을 실행해 통과를 확인했습니다. 외부 API를 호출하지 않는 함수 테스트이며, 전체 파이프라인을 검증하는 테스트와는 범위가 다릅니다.

```powershell
# 저장소 최상위에서 실행
cd agent_core
..\.venv\Scripts\python.exe -B test_agent_core.py
```

실행 실습에서는 정상 보고서 저장과 웹훅 연결 실패 시 보고서 보존을 확인했습니다. 테스트의 상세 범위와 한계는 [agent_core 검증 기록](agent_core/README.md#코드-리뷰와-테스트), 리뷰 경험과 개선 계획은 [1과목 회고](docs/day08_retrospective.md)에서 확인할 수 있습니다.

## 다음 개선 방향

- 입력 경로와 보고서 저장 경로를 설정으로 통합
- 설정 값과 LLM 응답의 형식·이벤트 누락 검증 강화
- 웹훅 HTTP 상태 확인, 재시도와 실패 로그 저장 연결
- 경계 조건과 오류 상황에 대한 테스트 확장

## 학습 자료 및 출처

[날짜별 학습 기록](docs/)과 [전체 실습 노트북 목록](agent_core/README.md#수업-노트북)을 함께 제공합니다.

SKT-ALEPH 1과목 수업 및 강사 제공 실습 자료를 바탕으로 작성했습니다. 강사 PDF 원문은 Git 저장소에 포함하지 않으며, 이 저장소는 실습 코드와 학습 결과를 정리합니다.
