"""
Checking remote machine
"""

import socket
from typing import Dict, Optional, Union

from is_it_up.base import IsItUpBase

_ = Dict, Union, Optional

class RemoteMachineChecker(IsItUpBase):
    def __init__(self, host: str, port: Union[str, int]):
        super(RemoteMachineChecker, self).__init__()
        pass