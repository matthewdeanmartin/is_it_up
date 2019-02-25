# coding=utf-8
"""
Checking remote machine
"""

import socket
from typing import List, Dict, Any

from is_it_up.base import IsItUpBase

_ = List, Dict, Any


class RemoteMachineChecker(IsItUpBase):
    def __init__(self, host: str, ports: List[str]) -> Dict[str, Any]:
        super(RemoteMachineChecker, self).__init__(host=host, ports=ports)
        self._resolve_dns_or_ip(host)
        self._ping(self._ipaddr)
        self._scan_ports(self._ipaddr, ports)
        print(self._state)
