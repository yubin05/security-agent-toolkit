# agent_core

SKT-ALEPH 1과목의 파이썬·로그 분석·AI 자동화 실습입니다. 2026년 9월 22일부터 10월 8일까지의 학습 과정과 보안 이벤트를 Markdown 보고서로 정리하는 파이프라인을 담았습니다.

## 보고서 파이프라인

```text
설정 읽기 → 이벤트 읽기 → LLM 이벤트 요약 → 위험도 정렬
→ 전체 개요 생성 → Markdown 보고서 저장 → 확인 대상 집계 → 웹훅 알림
```

현재 샘플 이벤트 6건은 한 배치로 요약합니다. 정상 실행 시 이벤트 요약과 전체 개요 생성에 LLM을 각각 한 번 호출하며, 위험도별 건수는 Python에서 계산합니다.

| 파일 | 역할 |
|---|---|
| [pipeline.py](pipeline.py) | 설정·입력·요약·보고서·알림을 연결하는 실행 진입점 |
| [llm_client.py](llm_client.py) | Gemini API 호출, API 키 읽기, JSON 응답 파싱 |
| [event_summarizer.py](event_summarizer.py) | 이벤트 배치 요약 및 high → medium → low 정렬 |
| [report_generator.py](report_generator.py) | 전체 개요 생성, 보고서 구성 및 저장 |
| [config.json](config.json) | 모델·확인 기준·보고서 폴더·웹훅 주소 설정 |
| [notifier.py](notifier.py) | 필수 설정 키 확인, 확인 대상 판정, 웹훅 전송 |
| [alert_server.py](alert_server.py) | 로컬 Flask 웹훅 수신 서버 |
| [test_agent_core.py](test_agent_core.py) | 외부 API 호출 없이 실행하는 assert 테스트 9건 |

이전 로그 파서, API 클라이언트, 도구 라우터, 스케줄러 실습은 아래 노트북에서 확인할 수 있습니다. `scheduler_job.py`는 별도 로그 탐지 실습이며, 보고서 파이프라인의 자동 실행에는 연결되어 있지 않습니다.

## 실행 방법

Python과 Gemini API 키가 필요합니다. Windows PowerShell에서 저장소 최상위 폴더를 기준으로 실행합니다. 가상환경이 없을 때 생성한 뒤 의존성을 설치합니다. `schedule`은 이전 스케줄러 실습에 사용합니다.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install requests flask schedule
```

저장소 최상위의 `.env`에 키를 설정합니다. 실제 키는 Git에 올리지 않습니다. `.env`는 `.gitignore`에 등록되어 있습니다.

```dotenv
GEMINI_API_KEY=발급받은_API_키
```

첫 번째 터미널에서 웹훅 수신 서버를 실행합니다.

```powershell
cd agent_core
..\.venv\Scripts\python.exe alert_server.py
```

두 번째 터미널도 저장소 최상위에서 시작해 보고서를 생성합니다.

```powershell
cd agent_core
..\.venv\Scripts\python.exe pipeline.py
```

수신 주소는 `http://127.0.0.1:5001/alert`입니다. 실행 시점의 날짜로 `daily_report_YYYYMMDD.md`를 현재 작업 폴더에 저장합니다. 입력은 날짜와 관계없이 `events_1008.json`으로 고정되어 있으므로 `agent_core` 폴더에서 실행합니다.

10월 8일 실습의 출력 예시입니다. 요약과 위험도 판정은 LLM 응답에 따라 달라질 수 있습니다.

```text
[보고서] daily_report_20261008.md 저장 · 사람 확인 필요 1건
```

결과 예시: [10월 8일 보고서](daily_report_20261008.md)

## 설정

| 설정 | 현재 값 | 동작 |
|---|---|---|
| `model` | `gemini-3.5-flash-lite` | LLM 호출 모델 |
| `approve_severity` | `high` | 지정 위험도 이상을 사람 확인 대상으로 집계 |
| `report_folder` | `reports` | 필수 키로 검사하지만 현재 저장 경로에는 미반영 |
| `webhook_url` | `http://127.0.0.1:5001/alert` | 보고서 저장 결과를 전송할 주소 |

확인 기준은 `low`, `medium`, `high`를 사용합니다. 확인 대상 판정에서 미등록 위험도는 `high`로 취급합니다. 현재는 확인 필요 건수를 알리며, 사람의 승인을 기다리거나 조치를 차단하는 절차는 구현하지 않았습니다.

## 코드 리뷰와 테스트

10월 8일 오후에 정적 리뷰, 함수 테스트, 실행 결과 확인, 논리 오류 디버깅을 실습했습니다.

```powershell
# agent_core 폴더에서 실행
..\.venv\Scripts\python.exe -B test_agent_core.py
```

| 대상 | 검증 내용 | assert 수 |
|---|---|---:|
| `make_lines` | 한 줄 형식, 빈 입력, 줄바꿈 포함 여부 | 3 |
| `needs_approval` | high·low 기준 판정, 미등록 위험도 처리 | 3 |
| `parse_llm_json` | 코드 블록 JSON, 일반 문장, 빈 문자열 처리 | 3 |

통과 시 `[테스트 통과] 9건 모두`를 출력합니다. 실패하면 해당 assert에서 중단합니다. 이 테스트는 LLM API와 웹훅을 호출하지 않으며, 전체 파이프라인 검증을 대신하지 않습니다. 두 이벤트의 줄바꿈 검사는 현재 존재 여부만 확인하므로 정확한 줄 수 검증으로 강화할 여지가 있습니다.

별도 실행 실습에서는 정상 보고서 저장을 확인했고, 연결할 수 없는 웹훅 주소에서 `ConnectionError`가 발생해도 보고서가 남는 것을 확인했습니다. [실패 상황 보고서](daily_report_20261009.md)의 날짜는 테스트에 전달한 날짜입니다. 디버깅 문제에서는 위험도 문자열의 공백·대소문자, 조건식 경계, 정렬 순서, 줄바꿈을 점검했습니다.

회고: [1과목 회고 및 개선 계획](../docs/day08_retrospective.md)

### 남은 개선점

- 설정 파일 누락·잘못된 JSON·값의 형식을 검증하고 오류 처리를 통일하기
- `report_folder`를 저장 경로에 반영하고 입력 이벤트 경로를 설정으로 분리하기
- 웹훅 HTTP 상태를 확인하기: 현재는 요청 예외만 실패로 처리해 HTTP 오류 상태를 놓칠 수 있음
- LLM 응답의 이벤트 ID·위험도·누락 여부를 검증하고 파싱 실패를 명확하게 보고하기
- 알림 재시도와 실패 로그 저장을 파이프라인에 연결하기: 별도 도전 실습과 회고에서 다뤘으며 현재 `notify`에는 미구현

## 수업 노트북

| 날짜 | 노트북 | 내용 |
|---|---|---|
| 9/22 | [변수와 리스트](260922_variables_and_lists.ipynb) | 변수·자료형·리스트·딕셔너리 |
| 9/23 오전 | [조건문과 반복문](260923_am_conditions_loops_counting.ipynb) | 조건문·반복문·Counter |
| 9/23 오후 | [함수와 파일](260923_pm_functions_files_csv.ipynb) | 함수·파일·모듈·CSV |
| 9/23 추가 | [도전 문제](260923_extra_challenges.ipynb) | 추가 연습 문제 |
| 9/28 오전 | [예외와 로깅](01_0928_am_exceptions_logging.ipynb) | 예외 처리·logging |
| 9/28 오후 | [중첩 자료구조와 JSON](02_0928_pm_nested_json.ipynb) | 중첩 자료구조·JSON·정규화 |
| 9/29 오전 | [정규식과 탐지 룰](01_0929_am_regex_detection_rules.ipynb) | 정규식·탐지 룰 |
| 9/29 오후 | [탐지 룰과 API](02_0929_pm_rules_api.ipynb) | 탐지 룰·API·HTTP 상태코드 |
| 9/30 오전 | [API 클라이언트](01_0930_am_requests_api_client.ipynb) | requests·API 클라이언트 |
| 10/2 오전 | [웹훅과 CLI](261002_am_webhook_cli.ipynb) | 웹훅·명령행 실행 |
| 10/2 오후 | [트리거와 스케줄러](261002_pm_trigger_scheduler.ipynb) | 주기 실행·탐지 트리거 |
| 10/6 오전 | [LLM과 프롬프트](261006_am_llm_prompt.ipynb) | LLM 호출·프롬프트 |
| 10/6 오후 | [에이전트 도구](261006_pm_agent_tools.ipynb) | 도구 선택·실행 |
| 10/7 오전 | [이벤트 요약](261007_am_report_summary.ipynb) | 배치 요약·위험도 정렬 |
| 10/7 오후 | [보고서 생성](261007_pm_report_generator.ipynb) | 개요·Markdown 보고서 |
| 10/8 오전 | [설정과 파이프라인](261008_am_config_pipeline.ipynb) | 설정 분리·확인 기준·알림 |
| 10/8 오후 | [리뷰·디버깅·회고](261008_pm_review_debug_retro.ipynb) | 코드 리뷰·테스트·논리 오류 수정·회고 |

노트북에는 모듈 파일을 생성하는 셀이 포함되어 있습니다. 다시 실행할 때는 기존 `.py` 파일을 덮어쓰는지 확인합니다. 선택 도전 과제의 완료 여부는 각 노트북의 실행 기록을 기준으로 확인합니다.

## 자료 출처

SKT-ALEPH 1과목 수업 및 강사 제공 실습 자료를 바탕으로 작성했습니다. 10월 8일 내용은 `1008-am-config-pipeline.pdf`, `1008-pm-review-debug-retro.pdf`와 실습 노트북을 참고했습니다. 강사 PDF 원문은 저장소에 포함하지 않으며, 이 README는 구현과 학습 결과를 정리한 문서입니다.
