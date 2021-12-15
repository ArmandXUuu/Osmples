from classes.CredentialAuthority import sign_signature
from utils.log_util import logger
from random import randint
from utils.const import *
from cryptoUtils.math_utils import pgcd_1


class Server:
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

    @staticmethod
    def set_certificate(cert_in: str) -> bool:  # TODO To delete.
        if Server.__certificate == "TODO, certificate to generate while init, TODO to rename to a identifiable string true":
            logger.critical("Critical failure when setting certificate : certificate already exists")
            return False

        Server.__certificate = cert_in
        return True
