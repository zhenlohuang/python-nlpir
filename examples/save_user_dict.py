#!/usr/bin/env python
#encoding: utf8

from PyNLPIR import *

if __name__ == '__main__':

    if init('../', Constants.CodeType.UTF8_CODE):
        print 'NLPIR initialization succeed.'
    else:
        raise 'NLPIR initialization fail.'

    succeed = save_user_dict()
    if succeed:
        print 'Save user dictionary successfully.'
    else:
        print 'Save user dictionary failed.'

    exit()
