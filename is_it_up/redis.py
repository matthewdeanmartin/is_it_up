# coding=utf-8
"""
After checking host, see if redis is responding.
"""
from is_it_up.base import IsItUpBase


class RedisChecker(IsItUpBase):
    def __init__(self, host, port, cloud):
        super(RedisChecker, self).__init__()
