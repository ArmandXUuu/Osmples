# Le serveur "A" :
# Il représente l'autorité d'administration de l'élection.

from classes.User import User, UserTypes
from classes.Server import Server
from cryptoUtils.hashage import generate_uuid
from utils.log_util import logger
from utils.const import p
from utils.debug import debug


class Bulletin:
    """
    class Bulletin :
        Is the object of 'bulletin'. It is the basic element of `Vote.bulletins`. It contains the choice
        of a voter `voter_uuid` in a specific vote `vote_id`.

    Attributes :
        vote_id : int, the id of the vote, is used to identify to which vote this bulletin belongs.
        voter_uuid : str, the uuid of the voter
        voter_code_vote : int, the vote code of the voter
        vote_chiffre : tuple, is the encrypted bulletin, contains the choice of voter *voter_uuid*
        signature : int, is the signature who proves the consciousness of `c_n`
    """
    vote_id = 0
    voter_uuid = ""
    voter_code_vote = 0

    vote_chiffre = ()
    signature = 0

    def __init__(self, vote_id: int, voter_uuid: str, voter_code_vote: int, vote_chiffre: tuple, signature):
        self.vote_id = vote_id
        self.voter_uuid = voter_uuid
        self.voter_code_vote = voter_code_vote
        self.vote_chiffre = vote_chiffre
        self.signature = signature


class Vote:
    """
    class Vote :
        It is the object of a vote, contains the information about :
            1. Basic infos of the vote like dates, candidates...
            2. A list of `vote_codes` which are the users registered in this vote, only them have access
               and rights to this vote.
            3. A list of `Bulletins` named after `bulletins`, it contains all the bulletins, which are
               the choices of users.
            4. `alphas` which is a dict, it is a dictionary {uuid: user.public_key} for all 'chargé de
               dépouillement' of this vote
    """
    id = 0

    candidates = {}
    __starts_at = ""
    __ends_at = ""
    __choices_possible = 1

    alphas = dict()
    vote_codes = []

    bulletins = []  # liste de type Bulletin

    def __init__(self, candidates: dict, starts_at: str, ends_at: str, choices_possible: int = 1):
        """
        Initiation, the unique way to input basic information of a vote. Which is to say we have no
        other way to change these infos.
        :param candidates: a dict which contains all of the candidates of this vote.
        :param starts_at: str, as its name suggests
        :param ends_at: str, as its name suggests
        :param choices_possible: int, is the possible number of choices a voter can made in this vote.
        """
        self.candidates = candidates
        self.__starts_at = starts_at
        self.__ends_at = ends_at
        self.__choices_possible = choices_possible

    def __str__(self):
        """
        Overwrites the __str__ methode. It gives a user-friendly str output of the basic
        information of this vote

        :return: A formatted string.
        """
        candidate_strings = []
        for k in self.candidates.keys():
            candidate_strings.append("\t\t" + str(k) + " - " + self.candidates[k])
        return "\033[1mInformations on this vote :\033[0m\n\t" \
               "You can only vote between {} and {}" \
               "\n\tCandidates are : \n\033[1;32m{}\033[0m\n\tYOU CAN JUST VOTE FOR \033[1;31m{}\033[0m PERSON(S) !\n" \
            .format(self.__starts_at, self.__ends_at,
                    '\n'.join(candidate_strings),
                    self.__choices_possible)

    def add_bulletin(self, bulletin: Bulletin):
        self.bulletins.append(bulletin)

    def get_bulletins(self) -> list:
        return self.bulletins

    def get_alpha(self) -> int:
        """
        It calculates the production of alphas of each 'chargé de dépouillement'
        $\alpha_{i}=g^{s_{i}}$ et $\alpha=\prod_{i} \alpha_{i}=\prod_{i} g^{s_{i}}=g^{\sum_{i} s_{i}}$
        :return: the alpha
        """
        alpha = 1
        for a in self.alphas.values():
            alpha *= a

        return alpha % p

    def get_candidates_num(self):
        return len(self.candidates)


class AdministrationServer(Server):
    """
    The server "\mathcal{A}".
    'l'authorité d'administration de l'élection'

    Attributes :
        user_infos : dict, {uuid: user}
        vote : Vote, the vote
    """
    user_infos = dict()  # a dict contains uuid and user : {uuid: user}
    vote = None

    def __init__(self):
        super().__init__("I am an AdministrationServer")
        logger.debug("An Administration Server was initiated")

    def add_user(self, user: User):
        """
        There are 2 types of users, see : ./classes/User.py `class UserTypes(IntEnum)`
        Here we generate user's `uuid`, and add to `user_infos`. If this user is a 'chargé de dépouillement', then
        store his/her alpha, the public key.
        :param user: type User
        """
        uuid = generate_uuid("user_Unique_ID for {}".format(user.__str__()))
        self.user_infos[uuid] = user  # for now we just deal with one vote a time. so no [[__user_list]] for now

        if user.user_type == UserTypes.TrustedDelegatedUser:
            self.vote.alphas[uuid] = user.public_key

        logger.debug(self.user_infos)

    def get_uuids(self):
        uuids = []
        for uuid in self.user_infos.keys():
            if self.user_infos[uuid].user_type == UserTypes.Voter:
                uuids.append(uuid)
        return uuids

    def __str__(self):
        return "In administrater server A we have : {} - {}".format(self.user_infos, self.user_infos)

    def set_vote(self):
        """
        Where we configure a vote.
        """
        if not debug:
            start_date = input("Date de début (YYYY-MM-DD) : ")
            end_date = input("Date de fin (YYYY-MM-DD) : ")
            candidates_input = input(
                "Saisir les candidats sous la forme 'nom prénom' et séparer chaque candidat par une virgule : ")
            liste_candidates = {}
            i = 1
            for candidat in candidates_input.split(','):
                liste_candidates[i] = candidat.strip()
                i += 1
            self.vote = Vote(liste_candidates, start_date, end_date)
        else:
            self.vote = Vote({1: "Macron", 2: "Obama", 3: "XI Jinping"}, "2021-11-11 00:00:00", "2022-01-01 12:59:59",
                             1)

    def get_vote(self):
        return self.vote
