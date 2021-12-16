from utils.const import p, g, q
from random import randint
from cryptoUtils.math_utils import fast_mod
from cryptoUtils.hashage import get_hashage_int


def generate_chal(s: int, uuid: str) -> tuple:
    """

    :param s: la signature
    :param uuid:
    :return:
    """
    w = randint(1, p)
    A = fast_mod(g, w)

    s_m_a = str(s) + uuid + str(A)

    return get_hashage_int(s_m_a), w


def zero_knowledge_verify(w: int, c_n, chal: int, s: int, uuid: str) -> bool:
    if type(c_n) is str:
        res = ""
        for char in c_n:
            res += str(ord(char))
        c_n = int(res)
    resp = (w - c_n * chal) % q

    # TODO implemente read fichier
    v_k = 8243664291748354336794431492811872647286141641553220057519948734082910426318802646795429630124460647871101857620651003817862859988640235054170588952677989279459221638287389266325954138266211732875990979890295389716603298205178968268079223632752061959127544254328600555233119500620081629830336371138975543783520411854820438505267776940299782049766458322102182558221150818164532555974999252035150822206253612357408188452761055422879475836921370048178201802730537311084972531800502145745549316459201411882509683949049399839777579433074484481465092904475269909660129619065365997595882759960340175981001974477955651034066

    A = (fast_mod(g, resp) * fast_mod(v_k, chal)) % p
    s_m_a_prime = str(s) + uuid + str(A)
    h_prime = get_hashage_int(s_m_a_prime)

    return h_prime == chal
