import logging
from collections import Counter

logging.basicConfig(
    filename="parser.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    encoding="utf-8",
)

def parser_line(line):
  parts = line.strip().split(",")

  re_dict = {}
  re_dict["time"] = parts[0]
  re_dict["user"] = parts[1]
  re_dict["event"] = parts[2]
  re_dict["ip"] = parts[3]

  return re_dict

file_name = "sample_logs_broken.csv"
with open(file_name, encoding="utf-8") as f:
  logging.info(f"파서 시작: {file_name}")

  count = 0
  fail_users = []
  for line in f:
    try:
      temp_dict = parser_line(line)

      if temp_dict["event"] == "LOGIN_FAIL":
        fail_users.append(temp_dict["user"])

      count += 1
    except IndexError:
      logging.warning(f"{line.strip()}")

  logging.info(f"정상 로그 {count}건 처리 완료")
  
  fail_users = Counter(fail_users)
  # print(fail_users)
  for user, count in fail_users.items():
    if count >= 3: print(f"	확인 필요: {user} — 실패 {count}회")
