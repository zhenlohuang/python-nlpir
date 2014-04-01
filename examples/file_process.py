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

    source_file = './resources/text.txt'
    target_file = './resources/text.txt.out'
    speed = file_process(source_file, target_file, True)
    if speed:
        print 'Processing speed: %d words/s' % speed
    else:
        print 'Processing failed.'

    exit()
