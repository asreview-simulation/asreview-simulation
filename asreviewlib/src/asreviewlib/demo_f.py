# this file is just a demonstration of private v public module files
# compare with demo_d/{_demo.py,__init__.py}
import sys


def fun():
    print(f"module {__name__} imports built-in module 'sys': {sys}")
