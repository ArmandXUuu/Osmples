import unittest
from User import User, UserTypes
from VoteServer import VoteServer as S
from AdministrationServer import AdministrationServer as A, Vote as V
from RegistrationServer import RegistrationServer as E
from utils.log_util import logger


class MyTestCase(unittest.TestCase):
    def test_something(self):
        # Server definition
        a = A()
        e = E()
        s = S()

        a.add_vote()

        user1 = User("Ziyi", "XU", "ziyi@avbc.abc", UserTypes.Voter)
        user2 = User("ThangLdong", "C", "abc@abc.abc", UserTypes.Voter)
        user3 = User("ThanagLong", "C", "abc@avbc.aybc", UserTypes.Voter)
        user4 = User("Than5gLdong", "C", "abc@abc.abc", UserTypes.Voter)
        user5 = User("ThanzgLong", "C", "abc@abc.abc", UserTypes.TrustedDelegatedUser)
        user6 = User("fsa", "C", "abc@abc.abc", UserTypes.TrustedDelegatedUser)
        user7 = User("fsadfsf", "C", "abc@abc.abc", UserTypes.TrustedDelegatedUser)
        user8 = User("fdfsdfsdfsdfsdf", "C", "abc@abc.abc", UserTypes.TrustedDelegatedUser)
        user9 = User("fdfefe", "C", "abc@abc.abc", UserTypes.TrustedDelegatedUser)

        a.add_user(user1)
        a.add_user(user2)
        a.add_user(user3)
        a.add_user(user4)
        a.add_user(user5)
        a.add_user(user6)
        a.add_user(user7)
        a.add_user(user8)
        a.add_user(user9)


        print(e.generate_credentials(a.get_uuids()))

        a.vote.vote_codes = e.generate_credentials(a.get_uuids())

        e.set_certificate("TODO, certificate to generate while init, TODO to rename to a identifiable string")

        test1 = a.vote.get_alpha()
        # certificat
        logger.debug(a.get_certificate())
        logger.debug(e.get_certificate())
        logger.debug(s.get_certificate())

        # a.get_vote_codes(e)


if __name__ == '__main__':
    unittest.main()
