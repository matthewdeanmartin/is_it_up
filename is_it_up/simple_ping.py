# coding=utf-8
"""
Quickly decide if NLP server is up or not.
"""
from is_it_up.base import IsItUpBase
from timeit import default_timer as timer

import socket
from typing import Dict, Union, Optional

_ = Dict, Union, Optional


class EC2Checker(IsItUpBase):
    def __init__(self, host: str, port: Union[str, int]):
        super(EC2Checker, self).__init__()
        return self.ping_nlp(host, int(port))[host] is not None

    def ping_nlp(
        self, hostname: str, port: int = 9000, timeout: float = 1.0
    ) -> Dict[str, Optional[float]]:
        start = timer()
        connection = socket.socket()
        connection.settimeout(timeout)
        try:
            connection.connect((hostname, port))
            end = timer()
            delta = end - start  # type: Optional[float]
        except ConnectionRefusedError:
            delta = None
        except (socket.timeout, socket.gaierror) as error:
            # logger.debug('telnet error: ', error)
            delta = None
        finally:
            connection.close()

        return {hostname: delta}
