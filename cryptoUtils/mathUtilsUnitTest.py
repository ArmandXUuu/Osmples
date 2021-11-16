import unittest
import math_utils
import time
from utils.log_util import logger


class MyTestCase(unittest.TestCase):
    def test_something(self):
        """
        time_start = time.time()
        print(math_utils.fast_mod(13789, 7223411, 2345))
        time_end = time.time()
        logger.debug("time cost {}".format(time_end - time_start))
        # time cost 4.00543212890625e-05

        print(13789 ** 7223411 % 2345)
        time_end = time.time()
        logger.debug("time cost {}".format(time_end - time_start))
        # time cost 59.1290009021759 - ATTENTION
        """


if __name__ == '__main__':
    unittest.main()
