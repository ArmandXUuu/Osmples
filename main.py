#!/usr/bin/python3
def show_welcoming_message():
    print("Bonjour ô maître Rémi ! Comment puis-je aider votre Sainteté ?")

def show_options():
    print("""->1<- Créer un vote.\n->2<- Enregistrer un électeur.\n->3<- Enregistrer un vote.\n->4<- Vérifier un vote.\n->5<- Procéder au dépouillement.\n->6<- Quitter le programme.""")

def start_vote_creation():
    print("Création du vote ...")

def start_elector_creation():
    print("Création d'un électeur...")

def start_vote_selection():
    print("Sélection d'un vote...")

def start_vote_verification():
    print("Vérification du vote...")

def start_vote_counting():
    print("Dépouillement du vote...")

def main():
    show_welcoming_message()
    has_been_terminated = False
    while not has_been_terminated:
        show_options()
        chosen_option = str(input())
        if "1" == chosen_option:
            start_vote_creation()
        elif "2" == chosen_option:
            start_elector_creation()
        elif "3" == chosen_option:
            start_vote_selection()
        elif "4" == chosen_option:
            start_vote_verification()
        elif "5" == chosen_option:
            start_vote_counting()
        elif "6" == chosen_option:
            has_been_terminated = True

main()
