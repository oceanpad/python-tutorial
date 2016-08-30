#!/usr/bin/env python3
# -*- coding: utf-8 -*-
' this is a comment '
__author__ = 'Frank Zhao'

import sys

def test():
    args = sys.argv
    if len(args)==1:
            print('Hello, world!')
            print(args)
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

print(__name__)

if __name__=='__main__':
    test()
