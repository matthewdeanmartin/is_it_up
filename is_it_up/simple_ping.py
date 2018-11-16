# coding=utf-8
"""
Quickly decide if NLP server is up or not.
"""
from timeit import default_timer as timer

import socket
from typing import Dict, Union, Optional

_ = Dict, Union, Optional


def quick_check(host: str, port: Union[str, int]) -> bool:
    return ping_nlp(host, int(port))[host] is not None


def ping_nlp(
    hostname: str, port: int = 9000, timeout: float = 1.0
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


if __name__ == "__main__":
    print(ping_nlp("localhost"))
