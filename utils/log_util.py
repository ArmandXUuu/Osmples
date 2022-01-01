import logging

formatter = logging.Formatter("\033[1;32m%(asctime)s %(levelname)s %(filename)s[line:%(lineno)d] - %(message)s\033[0m")

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
console = logging.StreamHandler()
console.setFormatter(formatter)
logger.addHandler(console)
