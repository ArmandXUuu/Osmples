import logging

formatter = logging.Formatter("\033[1;32m%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s - %(message)s\033[0m","%m/%d/%Y %I:%M:%S %p")

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
console = logging.StreamHandler()
console.setFormatter(formatter)
logger.addHandler(console)
