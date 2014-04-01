#!/usr/bin/env python
#encoding: utf8

from PyNLPIR import *
import os

if __name__ == '__main__':

    init_dir = os.path.join(os.path.dirname(__file__), os.path.pardir)
    if init(init_dir, Constants.CodeType.UTF8_CODE):
        print 'NLPIR initialization succeed.'
    else:
        raise 'NLPIR initialization fail.'

    filename = './resources/text.txt'
    print get_file_new_words(filename)

    exit()
