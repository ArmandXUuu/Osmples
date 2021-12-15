import unittest
from User import User, UserTypes
from VoteServer import VoteServer as S
from AdministrationServer import AdministrationServer as A
from RegistrationServer import RegistrationServer as E
from classes.CredentialAuthority import verify_certificate
from classes.RegistrationServer import generate_credentials
from utils.log_util import logger
from sys import setrecursionlimit
from cryptoUtils.el_gamal import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        setrecursionlimit(10000000)
        # Server definition
        a = A()
        e = E()
        s = S()

        a.set_vote()

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

        # print(e.generate_credentials(a.get_uuids()))

        a.vote.vote_codes = e.generate_credentials(a.get_uuids())

        # e.set_certificate("TODO, certificate to generate while init, TODO to rename to a identifiable string")

        test1 = a.vote.get_alpha()
        # certificat
        logger.debug("show certivicats")
        # logger.debug(a.get_certificate())
        # logger.debug(e.get_certificate())
        # logger.debug(s.get_certificate())

        certificate_a = a.get_certificate()

        reuslt = verify_certificate(*certificate_a)
        logger.debug(reuslt)

        # El Gamal - pour partager la clé pour Blowfish
        key = "test_el_gamal"
        res_encrypt = eg_encrypt(a.get_public_key(), key)

        res_decrypt = eg_decrypt(a.get_signature_x(), *res_encrypt)

        # a.get_vote_codes(e)

        # Use case for a user *u* :
        # *u* asks a server (for instance A) to return a certificate
        certificate_to_verify = a.get_certificate()
        # *u* contacts an "authorité de confiance" to validate the certificate received
        result = verify_certificate(*certificate_to_verify)
        # Information exchange between user *u* and server can be established by using BlowFish algorithm, if the
        # certificate is validated.
        if result:
            print("Validation succeeded")
        # If not, the server's public key (contained in the certificate) is uesd to "communiqué une clé sercrète"
        else:
            print("The validation failed !!")
            print("Franchement je ne comprends pas.")

        # Let's say that Eve changed the certificate
        certificate_modified = [list(certificate_to_verify[0]), list(certificate_to_verify[1]),
                                certificate_to_verify[2]]
        certificate_modified[1][1] += 1
        result = verify_certificate(*certificate_modified)
        if result:
            print("Validation succeeded")
        else:
            print("The validation failed !!")
            print("Franchement je ne comprends pas.")


if __name__ == '__main__':
    unittest.main()
