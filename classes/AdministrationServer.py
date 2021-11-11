# Le serveur "A" :
# Il représente l'autorité d'administration de l'élection.

from . import User
from cryptoUtils.hashage import generate_uuid
from utils.log_util import logger
from utils.file_rw_utils import json_output


class AdministrationServer:
    __user_info_list = dict()  # a dict contains uuid and user : {uuid: user}

    def __init__(self):
        print("initiate a Administration server")

    def add_user(self, user: User):
        uuid = generate_uuid("user_Unique_ID for {}".format(user.__str__()))
        self.__user_info_list[uuid] = user  # for now we just deal with one vote a time. so no [[__user_list]] for now
        logger.debug(self.__user_info_list)
        json_output(self.__user_info_list, True)

    def __str__(self):
        return "In administrater server A we have : {} - {}".format(self.__user_info_list, self.__user_info_list)