#!/usr/bin/python3
import os
from classes import AdministrationServer as A, RegistrationServer as E, VoteServer as S, User as U
from classes.RegistrationServer import generate_credentials
from utils.log_util import logger
from sys import setrecursionlimit

setrecursionlimit(10000000)

# Global variables
terminate_programe = False
a = A.AdministrationServer()
e = E.RegistrationServer()
s = S.VoteServer()

# debug variables
debug = True
logger.debug("This is the very begging of the program !")

vote_test = A.Vote({1: "Macron", 2: "Obama", 3: "XI Jinping"}, "2021-11-11 00:00:00", "2022-01-01 12:59:59", 1)


def show_welcoming_message():
    print("Bonjour ô maître Rémi ! Comment puis-je aider votre Sainteté ?")


def show_options():
    print(
        "->1<- Créer un vote.\n->2<- Enregistrer un électeur.\n->3<- Enregistrer un vote.\n->4<- Vérifier un "
        "vote.\n->5<- Procéder au dépouillement.\n->6<- Quitter le programme.")


def start_vote_creation():
    print_information("Création d'un vote ...")
    a.add_vote()


def start_elector_creation():
    print_information("Création d'un électeur...")
    if not debug:
        first_name = input("Please enter the first name : ")
        last_name = input("Please enter the last name : ")
        email = input("Please enter email : ")
        a.add_user(U.User(first_name, last_name, email, U.UserTypes.Voter))
    else:
        a.add_user(U.User("ziyi", "XU", "ziyi@drouot.com", U.UserTypes.Voter))
        a.add_user(U.User("ziy1i", "XU4", "ziyi1@drouot.com", U.UserTypes.Voter))
        a.add_user(U.User("ziyi2", "X4U", "ziy2i@drouot.com", U.UserTypes.Voter))
        a.add_user(U.User("ziy3i", "3XU", "z1iyi@d3rouot.com", U.UserTypes.Voter))
        a.add_user(U.User("ziy4i", "XU53", "ziyi42@drouot.com", U.UserTypes.TrustedDelegatedUser))
        a.vote.vote_codes = generate_credentials(a.get_uuids())


def user_definition_done():
    a.vote.vote_codes = generate_credentials(a.get_uuids())


def start_vote_selection():
    print_information("Sélection d'un vote...")
    choice = -1
    valide = False
    public_key = input("Saisir votre clé publique :")

    while choice == -1 and not valide:
        print(a.vote)
        choice = int(input("Faites votre choix : (1, 2, ou 3)"))
        if a.vote.get_candidates_num() >= choice > 0:
            valide = True
        else:
            choice = -1
            print("Faite votre choix parmis {} candidates".format(a.vote.get_candidates_num()))

    print_information("Votre choix est bien pris en compte !")


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
        "6": terminate_program,
        "user_definition_done": user_definition_done,
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
        execute_option(input("Faites votre choix : "))


if __name__ == "__main__":
    main()
