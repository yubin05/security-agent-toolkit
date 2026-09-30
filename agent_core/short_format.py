import logging

logging.basicConfig(
    filename="short.log",
    format="%(asctime)s %(message)s",
    encoding="utf-8",
)

logging.warning("warning 로 남긴 줄")
