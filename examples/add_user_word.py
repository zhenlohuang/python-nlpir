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

    word = '爱思客\tn'
    succeed = add_user_word(word)
    if succeed:
        print 'Add (%s) to user dictionary successfully.' % word
    else:
        print 'Add (%s) to user dictionary failed.' % word

    exit()
