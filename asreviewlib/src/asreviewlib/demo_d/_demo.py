# this file is just a demonstration of private v public module files
# compare with demo.py
import sys


def fun():
    print(f"module demo/_demo.py imports built-in module 'sys': {sys}")
