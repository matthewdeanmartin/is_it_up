# coding=utf-8
"""
Resource availability checker.

Usage:
  is_it_up.py (ec2 | remote_machine | redis | elasticache | database) <host> <ports>
  is_it_up.py -i | --input-file
  is_it_up.py -d | --dict
  is_it_up.py -h | --help
  is_it_up.py --version
Options:
  -i --input-file   Specify YAML file that contains parameters of resources to check them
  -d --dict         Specify dictionary that contains parameters of resources to check them
  -h --help         Show this screen.
  --version         Show version.

"""

import docopt

import is_it_up.__version__ as version
from is_it_up import (
    RedisChecker,
    RemoteMachineChecker,
)


def entry(*args, **kwargs):
    arguments = docopt.docopt(__doc__, version="Is_it_up {0}".format(version))
    print(arguments)


if __name__ == "__main__":
    entry()
