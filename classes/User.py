# Classe pour des utilisateurs (votant)
from enum import IntEnum
import random
from utils.const import *
from cryptoUtils.math_utils import fast_mod


class UserTypes(IntEnum):
    Voter = 1  # les voteurs \mathbb{V}_n
    TrustedDelegatedUser = 2  # les utilisateurs de confiance cahrgées du dépouillement \mathbb{T}_i


class User:
    __first_name = ""
    __last_name = ""
    __email = ""
    user_type = UserTypes

    __private_key = 0
    public_key = 0

    def __init__(self, first_name: str, last_name: str, email: str, user_type: UserTypes = UserTypes.Voter):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.user_type = user_type
        if user_type == UserTypes.TrustedDelegatedUser:
            self.__private_key = random.randint(2, p - 1)
            self.public_key = fast_mod(g, self.__private_key)

    def __str__(self):
        return "This user (type {}) is named after {} {}, his/her Email is {}. {} {}".format(self.user_type,
                                                                                             self.__first_name,
                                                                                             self.__last_name,
                                                                                             self.__email,
                                                                                             self.__private_key,
                                                                                             self.public_key
                                                                                             )
