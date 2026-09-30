import logging

logging.basicConfig(
    filename="agent.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    encoding="utf-8",
)

with open("sample_logs.csv", encoding="utf-8") as f:
  logging.info("집계 시작")
  count = 0
  for line in f:
    count += 1

  logging.info(f"집계 완료 {count}건")
