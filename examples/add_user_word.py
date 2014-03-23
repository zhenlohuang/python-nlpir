#!/usr/bin/env python
#encoding: utf8

from PyNLPIR import *

if __name__ == '__main__':

    if init('../', Constants.CodeType.UTF8_CODE):
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
