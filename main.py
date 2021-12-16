#!/usr/bin/python3
import os
from classes import AdministrationServer as A, RegistrationServer as E, VoteServer as S, User as U
from classes.VoteServer import encrypt_vote, decrypt_vote
from classes.AdministrationServer import Bulletin
from utils.log_util import logger
from sys import setrecursionlimit
from classes.CredentialAuthority import sign_signature
from random import randint
from utils.const import p
from cryptoUtils.math_utils import pgcd_1
from utils.file_rw_utils import json_read

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
    a.set_vote()


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
        user_definition_done()


def user_definition_done():
    a.vote.vote_codes = e.generate_credentials(a.get_uuids())
    s.set_vote(a.vote)


def start_vote_selection():
    print_information("Sélection d'un vote...")
    choice = -1
    valide = False
    uuid = input("Saisir votre uuid :")

    while choice == -1 and not valide:
        print(s.vote)
        choice = int(input("Faites votre choix : (1, 2, ou 3)"))
        if s.vote.get_candidates_num() >= choice > 0:
            valide = True
        else:
            choice = -1
            print("Faite votre choix parmis {} candidates".format(s.vote.get_candidates_num()))

    vote_encrypted = encrypt_vote(a.vote.get_alpha(), choice)
    c_n_int = json_read(uuid, "c_n_int")

    y = randint(2, p - 1)
    while pgcd_1(y, p - 1) != 1:
        y = randint(2, p - 1)
    s.vote.add_bulletin(Bulletin(a.vote.id, uuid, json_read(uuid, "code_vote"), vote_encrypted, sign_signature(vote_encrypted[1], c_n_int, y)))
    print_information("Votre choix est bien pris en compte !")


def start_vote_verification():
    print_information("Vérification du vote...")
    s.execute_audit()


def start_vote_counting():
    print_information("Dépouillement du vote...")
    s.counting()


def terminate_program():
    global terminate_programe
    terminate_programe = True
    print("\033[1;5;31m\tAu revoir !\033[0m")


def print_information(message: str):
    print("\033[32m%s\033[0m" % message)

def test_decrypt_bulletins():
    vote_tttest = s.vote
    for bulletin in vote_tttest.get_bulletins():
        print(decrypt_vote(11, *bulletin.vote_chiffre))
        print("dsafads")



def execute_option(index: str):
    options = {
        "1": start_vote_creation,
        "2": start_elector_creation,
        "3": start_vote_selection,
        "4": start_vote_verification,
        "5": start_vote_counting,
        "6": terminate_program,
        "user_definition_done": user_definition_done,
        "test_decrypt_bulletins": test_decrypt_bulletins
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
