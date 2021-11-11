import unittest
from User import User, UserTypes
from VoteServer import VoteServer as S
from AdministrationServer import AdministrationServer as A
from RegistrationServer import RegistrationServer as E

class MyTestCase(unittest.TestCase):
    def test_something(self):
        user1 = User("Ziyi", "XU", "ziyi@abc.abc", UserTypes.Voter)
        print(user1)
        voteServer = S()


if __name__ == '__main__':
    unittest.main()


