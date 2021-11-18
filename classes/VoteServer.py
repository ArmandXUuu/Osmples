# Le serveur "S" :
# Il est le serveur de vote, celui sur les électeur mettent leur bulletin

from classes.Server import Server


class VoteServer(Server):

    def __init__(self):
        print("initiate a vote server")