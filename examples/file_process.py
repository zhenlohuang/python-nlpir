#!/usr/bin/env python
#encoding: utf8

from PyNLPIR import *

if __name__ == '__main__':

    if init('../', Constants.CodeType.UTF8_CODE):
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
