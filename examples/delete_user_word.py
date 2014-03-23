#!/usr/bin/env python
#encoding: utf8

from PyNLPIR import *

if __name__ == '__main__':

    if init('../', Constants.CodeType.UTF8_CODE):
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
