# this file is just a demonstration of private v public module files
# compare with demo_f.py
import sys


def fun():
    print(f"module {__name__} imports built-in module 'sys': {sys}")
