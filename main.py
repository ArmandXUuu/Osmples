#!/usr/bin/python3
import os
from classes import AdministrationServer as A, RegistrationServer as E, VoteServer as S, User as U
from utils.log_util import logger


# Global variables
terminate_programe = False
a = A.AdministrationServer()
e = E.RegistrationServer()
s = S.VoteServer()

# debug variables
debug = False
logger.debug("This is the very begging of the program !")

def show_welcoming_message():
    print("Bonjour ô maître Rémi ! Comment puis-je aider votre Sainteté ?")


def show_options():
    print(
        "->1<- Créer un vote.\n->2<- Enregistrer un électeur.\n->3<- Enregistrer un vote.\n->4<- Vérifier un "
        "vote.\n->5<- Procéder au dépouillement.\n->6<- Quitter le programme.")


def start_vote_creation():
    print_information("Création du vote ...")


def start_elector_creation():
    print_information("Création d'un électeur...")
    if not debug:
        first_name = input("Please enter the first name :")
        last_name = input("Please enter the last name :")
        email = input("Please enter email :")
        a.add_user(U.User(first_name, last_name, email, U.UserTypes.Voter))
    else:
        a.add_user(U.User("ziyi", "XU", "ziyi@drouot.com", U.UserTypes.Voter))


def start_vote_selection():
    print_information("Sélection d'un vote...")


def start_vote_verification():
    print_information("Vérification du vote...")


def start_vote_counting():
    print_information("Dépouillement du vote...")


def terminate_program():
    global terminate_programe
    terminate_programe = True
    print("\033[1;5;31m\tAu revoir !\033[0m")


def print_information(message: str):
    print("\033[32m%s\033[0m" % message)


def execute_option(index: str):
    options = {
        "1": start_vote_creation,
        "2": start_elector_creation,
        "3": start_vote_selection,
        "4": start_vote_verification,
        "5": start_vote_counting,
        "6": terminate_program
    }

    method = options.get(index)
    if method:
        method()
    else:
        print("\033[1;5;31m\n\tEntrée invalide ;)\n\tOn recommence !\n\n\033[0m")  # https://www.cnblogs.com/wj-1314/p/7449812.html
        os.system("sleep 2 && clear")


def main():
    show_welcoming_message()
    while not terminate_programe:
        show_options()
        chosen_option = input("Faites votre choix : ")
        execute_option(chosen_option)


if __name__ == "__main__":
    main()
