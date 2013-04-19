#!/usr/bin/env python
#coding:utf-8
'''
Created on Fri 19, 2013

@author: killua
@e-mail: killua_hzl@163.com
@Decription: Python for NLPIR
'''
import NLPIR
import os

def nlpir_init(init_dir = '.', code_type = 'GBK'):
    '''
    Init the analyzer and prepare necessary data for NLPIR according the configure file.
    '''
    if code_type == 'GBK':
        is_succeed = NLPIR.NLPIR_Init(init_dir, NLPIR.GBK_CODE)
    elif code_type == 'UTF-8' or code_type == 'UTF8':
        is_succeed = NLPIR.NLPIR_Init(init_dir, NLPIR.UTF8_CODE)
    elif code_type == 'BIG5':
        is_succeed = NLPIR.NLPIR_Init(init_dir, NLPIR.BIG5_CODE)
    elif code_type == 'GBK_FANTI':
        is_succeed = NLPIR.NLPIR_Init(init_dir, NLPIR.GBK_FANTI_CODE)
    if is_succeed:
        print 'NLPIR Successful.'
    else:
        print 'NLPIR Failed.'

def nlpir_exit():
    '''
    Exit the program and free all resources and destroy all working buffer used in NLPIR.    
    '''
    return NLPIR.NLPIR_Exit()

def nlpir_import_user_dict(user_dict):
    '''
    Import user-defined dictionary from a text file. 
    '''
    return NLPIR.NLPIR_ImportUserDict(user_dict)

def nlpir_paragraph_process(text, is_pos_tagged = False):
    '''
    Process a paragraph
    '''
    return NLPIR.NLPIR_ParagraphProcess(text, is_pos_tagged)

def nlpir_file_process(source_file, target_file, is_pos_tagged = False):
    '''
    Process a text file
    '''
    return NLPIR.NLPIR_FileProcess(source_file, target_file, is_pos_tagged)

def nlpir_add_user_word(word):
    '''
    Add a word to the user dictionary.
    '''
    return NLPIR.NLPIR_AddUserWord(word)

def nlpir_save_user_dict():
    '''
    Save the user dictionary to disk.
    '''
    return NLPIR.NLPIR_SaveTheUsrDic()

def nlpir_delete_user_word(word):
    '''
    Delete a word from the  user dictionary.
    '''
    return NLPIR.NLPIR_DelUsrWord(word)
