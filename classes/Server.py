from classes.CredentialAuthority import sign_signature
from random import randint
from utils.const import *
from cryptoUtils.math_utils import pgcd_1


class Server:
    """
    The super class of all servers : `AdministrationServer`, `RegistrationServer`, `VoteServer`
    A server has a certificate and its required variables.
    """
    __certificate = ()
    __signature_x = 0
    __signature_y = 0

    public_key = ()
    __private_key = 0
    signature = ()

    def __init__(self, message="This is a Random message TODO"):
        self.__signature_x = randint(2, p - 2)
        self.__private_key = self.__signature_x
        self.__signature_y = randint(2, p - 1)
        while pgcd_1(self.__signature_y, p - 1) != 1:
            self.__signature_y = randint(2, p - 1)

        self.public_key, self.signature = sign_signature(message, self.__signature_x, self.__signature_y)
        self.__certificate = self.public_key, self.signature, message

    def get_certificate(self) -> tuple:
        return self.__certificate

    def get_public_key(self) -> int:
        return self.public_key[2]  # c'est le `h`

    def get_signature_x(self) -> int:
        return self.__signature_x
