# coding=utf-8
"""
Wrapper for various check actions for different objects.
"""
import os
import socket
import subprocess
from typing import Optional, Dict, List
from is_it_up import IsItUpException

_ = Optional, Dict, List


class IsItUpBase(object):
    def __init__(
        self,
        host: str,
        ports: Optional[List[str]] = None,
        timeout: Optional[float] = None,
    ) -> None:

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

    def __ping(self, host: str, times: int = 1, timeout: int = 2000) -> None:
        if os.name == "posix":
            cmd = f"ping -c {times} -W {timeout} {host}"
        elif os.name in ("nt", "dos", "ce"):
            cmd = f"ping -n {times} -w {timeout} {host}"

        result = subprocess.call(cmd, shell=True)
        if result == 0:
            self._state["ping"] = True
        else:
            self._state["ping"] = False

    def __scan_ports(self, host: str, ports: List[str], timeout: float = 1.0) -> None:
        int_ports = []

        for i in ports:
            if i.count("-") == 1:
                first_port, last_port = i.split("-")
                if first_port.isdigit() and last_port.isdigit():
                    first_port = int(first_port)
                    last_port = int(last_port)
                else:
                    raise IsItUpException(f"Wrong port range for {host}")
                int_ports = int_ports + list(range(first_port, last_port + 1))
            elif i.count("-") == 0:
                if i.isdigit():
                    int_ports.append(int(i))
                else:
                    raise IsItUpException(f"Wrong port range for {host}")
            else:
                raise IsItUpException(f"Wrong port range for {host}")

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        checked_ports = {key: False for key in int_ports}
        for port in int_ports:
            result = s.connect_ex((host, port))
            if result == 0:
                checked_ports[port] = True
        s.close()

        self._state["scanned_ports"] = checked_ports
