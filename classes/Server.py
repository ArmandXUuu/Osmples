from utils.log_util import logger


class Server:
    __certificate = "TODO, certificate to generate while init, TODO to rename to a identifiable string true"

    @staticmethod
    def get_certificate() -> str:
        return Server.__certificate

    @staticmethod
    def set_certificate(cert_in: str) -> bool:
        if Server.__certificate == "TODO, certificate to generate while init, TODO to rename to a identifiable string true":
            logger.critical("Critical failure when setting certificate : certificate already exists")
            return False

        Server.__certificate = cert_in
        return True
