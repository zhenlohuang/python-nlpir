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
    succeed = delete_user_word(word)
    if succeed != -1:
        print 'Delete (%s) from user dictionary successfully.' % word
    else:
        print '(%s) not exist in the user dictionary.' % word

    add_user_word(word)
    succeed = delete_user_word(word)
    if succeed != -1:
        print 'Delete (%s) from user dictionary successfully.' % word
    else:
        print '(%s) not exist in the user dictionary.' % word

    exit()
