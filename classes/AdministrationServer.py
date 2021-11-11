# Le serveur "A" :
# Il représente l'autorité d'administration de l'élection.

from User import User


class AdministrationServer:
    __user_list = []

    def __init__(self):
        print("initiate a Administration server")

    def add_user(self, user: User):
        self.__user_list.append(user)
