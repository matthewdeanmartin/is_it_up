# coding=utf-8
"""
Resource availability checker.

Usage:
  is_it_up <resource> <host> <ports>
  is_it_up -i FILE
  is_it_up -d
  is_it_up -h
  is_it_up --version
Options:
  -i FILE --input-file=FILE   Specify YAML file that contains parameters of resources to check them
  -d --dict                   Specify dictionary that contains parameters of resources to check them
  -h --help                   Show this screen.
  --version                   Show version.

"""

import docopt

import is_it_up.__version__ as version


def entry(*args, **kwargs):
    arguments = docopt.docopt(__doc__, version="Is_it_up {0}".format(version))
    if arguments["<resource>"] == "remote_machine":
        from is_it_up.remote_machine import RemoteMachineChecker
    obj = RemoteMachineChecker(
        host=arguments["<host>"], ports=arguments["<ports>"].split(",")
    )
    return


if __name__ == "__main__":
    entry()
