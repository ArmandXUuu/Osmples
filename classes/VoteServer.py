# Le serveur "S" :
# Il est le serveur de vote, celui sur les électeur mettent leur bulletin

from classes.Server import Server
from utils.log_util import logger


class VoteServer(Server):

    def __init__(self):
        super().__init__("I am a VoteServer")
        logger.debug("A Vote Server was initiated")