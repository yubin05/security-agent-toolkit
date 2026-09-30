import re
import json

PATTERN = r"(?P<time>[\d:]+) (?P<level>[\w]+) [\w]+ login for (?P<user>[\w.]+) from (?P<ip>[\d.]+)"  # 여기를 채우세요

def parse_raw_logs(line):
    # 여기를 채우세요
    m = re.search(PATTERN, line)
    if m:
      return m.groupdict()
    else:
      return None
    

# rows와 unmatched를 만들고 파일 두 개로 저장하는 코드를 이어서 작성합니다.
result = []
unmatched_result = []

file_name = "raw_logs.txt"
with open(file_name, encoding="utf-8") as f:

  for line in f:
    origin_line = line
    line = line.strip()
    # parts = line.split()
    
    m = parse_raw_logs(line)
    if m:
      result.append(m)
    else:
      unmatched_result.append(origin_line)

# 정규화 파일 작성
file_name = "normalized_logs.json"
with open(file_name, "w", encoding="utf-8") as f:
  json.dump(result, f, ensure_ascii=False, indent=2)
print(f"정규화 {len(result)}건")

# 안 맞음 파일 작성
file_name = "unmatched_logs.txt"
with open(file_name, "w", encoding="utf-8") as f:
  for line in unmatched_result:
    f.write(line)
print(f"안 맞음 {len(unmatched_result)}건")
