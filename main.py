#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    References
        INPUT YOUR REFERNCE PAGES
"""
__version__ = '0.1.0.0a0'

import sys
"""
from <directoy>.<filename> import <class>
from <directoy>.<filename> import <function name>
"""
from ref_method.ref_method import hello
from ref_class.ref_class import ClassName
from module1.module1 import func1
from module2.module2 import func2
from module3.module3 import func3

reload(sys)
sys.setdefaultencoding('utf-8')


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


def main(argv=None):
    ref_class = ClassName()
    ref_class.helloWorld()
    hello()
    func1()
    func2()
    func3()

if __name__ == "__main__":
    sys.exit(main())
