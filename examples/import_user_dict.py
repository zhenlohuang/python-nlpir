#!/usr/bin/env python
#encoding: utf8

from PyNLPIR import *

if __name__ == '__main__':

    if init('../', Constants.CodeType.UTF8_CODE):
        print 'NLPIR initialization succeed.'
    else:
        raise 'NLPIR initialization fail.'

    text = '24小时降雪量24小时降雨量863计划ABC防护训练APEC会议BB机BP机C2系统C3I系统C3系统C4ISR系统C4I系统CCITT建议'
    print 'Before adding User-defined lexicon, the result is'
    print paragraph_process(text, True)
    num_items = import_user_dict('resources/userdict.txt')
    print '%d user-defined lexical entries added!' % num_items
    print 'After adding User-defined lexicon, the result is'
    print paragraph_process(text, True)

    exit()
