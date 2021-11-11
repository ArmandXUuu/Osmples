import unittest
from User import User, UserTypes
from VoteServer import VoteServer as S
from AdministrationServer import AdministrationServer as A
from RegistrationServer import RegistrationServer as E


class MyTestCase(unittest.TestCase):
    def test_something(self):
        user1 = User("Ziyi", "XU", "ziyi@abc.abc", UserTypes.Voter)
        user2 = User("ThangLong", "C", "abc@abc.abc", UserTypes.Voter)
        voteServer = S()
        a = A()
        a.add_user(user1)
        a.add_user(user2)


if __name__ == '__main__':
    unittest.main()
