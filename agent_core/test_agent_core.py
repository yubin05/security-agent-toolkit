import llm_client                                             # 오전에 만든 llm_client.py 를 불러온다
import notifier                                               # 3교시에 만든 notifier.py 를 불러온다
import report_generator                                       # 오후에 만든 report_generator.py 를 불러온다

# 1. 문제 5-3 의 assert 세 줄을 옮기세요 (sample · two 도 함께)
# ── 미리 채워 둔 줄입니다. 고치지 않습니다 ──
sample = [{"id": "E01", "risk_level": "High", "summary": "로그인 실패 4회"}]   # 대문자가 섞인 요약 한 건
two = [{"id": "E02", "risk_level": "low", "summary": "새 IP 로그인"}, {"id": "E03", "risk_level": "medium", "summary": "심야 접속"}]   # 요약 두 건
# ── 여기까지 ──

# 1. report_generator.make_lines(sample) 이 "- [HIGH] E01 로그인 실패 4회\n" 과 같은지 assert 로 확인하세요. 메시지는 "make_lines 결과가 다르다"
assert report_generator.make_lines(sample) == "- [HIGH] E01 로그인 실패 4회\n", "make_lines 결과가 다르다"

# 2. 빈 리스트 [] 를 넣으면 빈 문자열 "" 이 나오는지 assert 로 확인하세요. 메시지는 "빈 리스트는 빈 문자열이어야 한다"
assert report_generator.make_lines([]) == "", "빈 리스트는 빈 문자열이어야 한다"

# 3. 요약 두 건 two 를 넣으면 줄이 두 개(\n 이 두 개)인지 assert 로 확인하세요. 메시지는 "한 건에 한 줄이어야 한다"
assert "\n" in report_generator.make_lines(two), "한 건에 한 줄이어야 한다"



# 2. 문제 5-4 의 assert 세 줄을 옮기세요 (config 도 함께)
# ── 미리 채워 둔 줄입니다. 고치지 않습니다 ──
config = {"approve_severity": "high"}                       # 기준만 있으면 판정할 수 있다
# ── 여기까지 ──

# 1. needs_approval("high", config) 가 True 인지 assert 로 확인하세요
assert notifier.needs_approval("high", config)

# 2. needs_approval("low", config) 가 False 인지 assert 로 확인하세요
assert notifier.needs_approval("low", config) is False

# 3. 처음 보는 위험도 "critical" 이 True 인지 assert 로 확인하세요
assert notifier.needs_approval("critical", config)



# 3. 문제 5-5 의 assert 세 줄을 옮기세요 (fenced 도 함께)
# ── 미리 채워 둔 줄입니다. 고치지 않습니다 ──
fenced = "```json\n{\"tool\": \"lock_account\"}\n```"          # LLM 이 자주 보내는 모양 — 코드 블록에 싸인 JSON
# ── 여기까지 ──

# 1. parse_llm_json(fenced) 가 {"tool": "lock_account"} 와 같은지 assert 로 확인하세요
assert llm_client.parse_llm_json(fenced) == {"tool": "lock_account"}

# 2. parse_llm_json("그럴듯한 문장입니다") 가 None 인지 assert 로 확인하세요 (is None)
assert llm_client.parse_llm_json("그럴듯한 문장입니다") is None

# 3. parse_llm_json("") 가 None 인지 assert 로 확인하세요
assert llm_client.parse_llm_json("") is None

print("[테스트 통과] 9건 모두")                                       # 여기까지 오면 아홉 줄이 모두 참이었다
