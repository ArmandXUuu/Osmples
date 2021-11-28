import crypt as cr
import hashlib
import numpy as np


def hashage(input_message: str):
    hash_instance = hashlib.sha256()
    hash_instance.update(input_message.encode('utf-8'))
    return hash_instance


def generate_uuid(clair_info: str) -> str:  # TODO
    # return cr.crypt(clair_info, cr.mksalt(cr.METHOD_SHA512)) it's bizarre, with different input we haeve the same result ???
    hash_instance = hashage(clair_info)
    return hash_instance.hexdigest()


def get_hashage_int(message: str) -> int:
    """
    This function takes a string as input, which is the message to be hash-ed. It outputs an int
    which is the ASCII code of the result of the hash-ed message
    :param message: a string, as its name suggests
    :return: The ASCII code of the result of the hash-ed message, concatenated
    """
    hash_instance = hashage(message)
    res_array = np.fromstring(hash_instance.hexdigest(), dtype=np.uint8)
    result = ""
    for res in res_array:
        result += str(res)
    return int(result)
