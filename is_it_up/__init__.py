# coding=utf-8
"""
Check if server is up in many sense of the word
"""
from is_it_up.redis_ping import *
from is_it_up.simple_ping import *

import is_it_up.__version__ as version

__version__ = version.__version__
