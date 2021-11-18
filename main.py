#!/usr/bin/python3
import os
from classes import AdministrationServer as A, RegistrationServer as E, VoteServer as S, User as U
from utils.log_util import logger


# Global variables
terminate_programe = False
a = A.AdministrationServer()
e = E.RegistrationServer()
s = S.VoteServer()
vote_list = []
g = 2402352677501852209227687703532399932712287657378364916510075318787663274146353219320285676155269678799694668298749389095083896573425601900601068477164491735474137283104610458681314511781646755400527402889846139864532661215055797097162016168270312886432456663834863635782106154918419982534315189740658186868651151358576410138882215396016043228843603930989333662772848406593138406010231675095763777982665103606822406635076697764025346253773085133173495194248967754052573659049492477631475991575198775177711481490920456600205478127054728238140972518639858334115700568353695553423781475582491896050296680037745308460627

p = 20694785691422546401013643657505008064922989295751104097100884787057374219242717401922237254497684338129066633138078958404960054389636289796393038773905722803605973749427671376777618898589872735865049081167099310535867780980030790491654063777173764198678527273474476341835600035698305193144284561701911000786737307333564123971732897913240474578834468260652327974647951137672658693582180046317922073668860052627186363386088796882120769432366149491002923444346373222145884100586421050242120365433561201320481118852408731077014151666200162313177169372189248078507711827842317498073276598828825169183103125680162072880719

q = 78571733251071885079927659812671450121821421258408794611510081919805623223441  # TODO vérifie si nécessaire

# debug variables
debug = True
logger.debug("This is the very begging of the program !")

vote_test = A.Vote(["Macron", "Obama", "XI Jinping"], "2021-11-11 00:00:00", "2022-01-01 12:59:59", 1)

def show_welcoming_message():
    print("Bonjour ô maître Rémi ! Comment puis-je aider votre Sainteté ?")


def show_options():
    print(
        "->1<- Créer un vote.\n->2<- Enregistrer un électeur.\n->3<- Enregistrer un vote.\n->4<- Vérifier un "
        "vote.\n->5<- Procéder au dépouillement.\n->6<- Quitter le programme.")


def start_vote_creation():
    print_information("Création du vote ...")
    start_date = input("Date de début (YYYY-MM-DD) : ")
    end_date = input("Date de fin (YYYY-MM-DD) : ")
    candidats_input = input("Saisir les candidats sous la forme 'nom prénom' et séparer chaque candidat par une virgule : ")
    liste_candidats = []
    for candidat in candidats_input.split(','):
        liste_candidats.append(candidat.strip())
    vote_list.append(A.Vote(liste_candidats, start_date, end_date))



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
        a.add_user(U.User("ziy4i", "XU53", "ziyi42@drouot.com", U.UserTypes.Voter))


def start_vote_selection():
    print_information("Sélection d'un vote...")
    if not debug:
        for vote in vote_list:
            print(vote)
    else:
        print(vote_test)

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
