# this file is just a demonstration of private v public module files
# compare with demo/{_demo.py,__init__.py}
import sys


def fun():
    print(f"module demo.py imports built-in module 'sys': {sys}")
