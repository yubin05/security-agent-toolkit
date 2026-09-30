import logging

logging.basicConfig(
    filename="only_error.log",
    level=logging.ERROR,
    format="%(asctime)s %(levelname)s %(message)s",
    encoding="utf-8",
)

logging.info("info 로 남긴 줄")
logging.warning("warning 로 남긴 줄")
logging.error("error 로 남긴 줄")
