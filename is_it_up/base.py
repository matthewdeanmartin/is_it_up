"""
Wrapper for various check actions for different objects.
"""
import socket
from typing import Optional, Dict


class IsItUpBase(object):
    def __init__(self, host: str, options: Optional[Dict[str, str]] = None) -> None:

        self._state = {"available": False}
        self._hostname = None
        self._ipaddr = None

    def __resolve_dns_or_ip(self, host: str) -> None:
        try:
            result = socket.inet_aton(host)
            self._ipaddr = host
            self._hostname = self.__get_hostname(host)
        except socket.error:
            self._ipaddr = self.__get_ip(host)
            self._hostname = host

    def __get_ip(self, domain: str) -> Optional[str]:
        try:
            ip = socket.gethostbyname(domain)
            return ip
        except Exception:
            return None

    def __get_hostname(self, ipaddr: str) -> Optional[str]:
        try:
            hostname = socket.gethostbyaddr(ipaddr)[0]
            return hostname
        except Exception:
            return None
