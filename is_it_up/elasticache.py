# coding=utf-8
"""
Elasticache health check using cloudwatch metrics
"""

import socket
from typing import Dict, Optional, Union

from is_it_up.redis import RedisChecker

_ = Dict, Union, Optional


class ElastiCacheChecker(RedisChecker):
    def __init__(self, host: str, port: Union[str, int]):
        super(EC2Checker, self).__init__()
        pass
