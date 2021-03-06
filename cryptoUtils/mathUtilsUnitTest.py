import unittest
import math_utils
import time
from utils.log_util import logger
import random
import blow_fish
import hashage
from sys import setrecursionlimit
import zero_knowledge
import el_gamal



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
        g = 2402352677501852209227687703532399932712287657378364916510075318787663274146353219320285676155269678799694668298749389095083896573425601900601068477164491735474137283104610458681314511781646755400527402889846139864532661215055797097162016168270312886432456663834863635782106154918419982534315189740658186868651151358576410138882215396016043228843603930989333662772848406593138406010231675095763777982665103606822406635076697764025346253773085133173495194248967754052573659049492477631475991575198775177711481490920456600205478127054728238140972518639858334115700568353695553423781475582491896050296680037745308460627

        p = 20694785691422546401013643657505008064922989295751104097100884787057374219242717401922237254497684338129066633138078958404960054389636289796393038773905722803605973749427671376777618898589872735865049081167099310535867780980030790491654063777173764198678527273474476341835600035698305193144284561701911000786737307333564123971732897913240474578834468260652327974647951137672658693582180046317922073668860052627186363386088796882120769432366149491002923444346373222145884100586421050242120365433561201320481118852408731077014151666200162313177169372189248078507711827842317498073276598828825169183103125680162072880719

        setrecursionlimit(10000000)
        print(math_utils.fast_mod(g, random.randint(2, g-1), p))
        # logger.debug(hashage.get_hashage_int("THIS IS A test 123"))
        # logger.debug(signature.sign_signature("message"))

        # public_key, sig = signature.sign_signature("message")
        # logger.debug(public_key)
        # logger.debug(sig)
        # result_1 = signature.verify_certificate(public_key, sig, "message")
        # result_2 = signature.verify_certificate(public_key, sig, "messssss")
        # logger.debug(result_1)
        # logger.debug(result_2)
        # these test are not upated, after the changement of the signature of the function sign_signature() and verify_certificate()


        block = "testabck"

        # MINE
        bf = blow_fish.BlowFish("Key must be between 4 and 56 bytes long.")
        out = bf.encrypt(block)
        out_string = ''.join(out)
        # out_bytes = bytes(out_string, "unicode")
        # rint(out_bytes)

        res = bf.decrypt(out_string)
        print(res)


        zero_knowledge.test()



if __name__ == '__main__':
    unittest.main()
