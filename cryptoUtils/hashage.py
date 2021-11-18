import crypt as cr
import hashlib


def generate_uuid(clair_info: str) -> str:  # TODO
    # return cr.crypt(clair_info, cr.mksalt(cr.METHOD_SHA512)) it's bizarre, with different input we haeve the same result ???
    hash = hashlib.sha256()
    hash.update(clair_info.encode('utf-8'))
    return hash.hexdigest()
