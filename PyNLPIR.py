#!/usr/bin/env python
#coding:utf-8
'''
@author: killua
@e-mail: killua_hzl@163.com
@Decription: python wrapper for NLPIR.
'''
import NLPIR
import platform

class Constants(object):
    class POS(object):
        POS_MAP_NUMBER = NLPIR.POS_MAP_NUMBER
        ICT_POS_MAP_FIRST = NLPIR.ICT_POS_MAP_FIRST
        ICT_POS_MAP_SECOND = NLPIR.ICT_POS_MAP_SECOND
        PKU_POS_MAP_SECOND = NLPIR.PKU_POS_MAP_SECOND
        PKU_POS_MAP_FIRST = NLPIR.PKU_POS_MAP_FIRST
        POS_SIZE = NLPIR.POS_SIZE

    class CodeType(object):
        GBK_CODE = NLPIR.GBK_CODE
        UTF8_CODE = NLPIR.UTF8_CODE
        BIG5_CODE = NLPIR.BIG5_CODE
        GBK_FANTI_CODE = NLPIR.GBK_FANTI_CODE


def init(init_dir='.', encoding=Constants.CodeType.GBK_CODE):
    """
    Init the analyzer and prepare necessary data for NLPIR according the configure file.
    Parameters:
        init_dir: Initial Directory Path, where file Configure.xml and Data directory stored,
                  the default value is current working directory path.
        encoding: encoding of input string, default is GBK, and it can be set with UTF8 and BIG5.
    Return: Return true if init succeed. Otherwise return false.
    """
    return NLPIR.NLPIR_Init(init_dir, encoding)


def exit():
    """
    Exit the program and free all resources and destroy all working buffer used in NLPIR.
    Parameters: none
    Return: Return true if succeed. Otherwise return false.
    """
    return NLPIR.NLPIR_Exit()


def import_user_dict(user_dict):
    """
    Import user-defined dictionary from a text file.
    Parameters: Text filename for user dictionary.
    Return: The number of lexical entry imported successfully.
    """
    return NLPIR.NLPIR_ImportUserDict(user_dict)


def paragraph_process(text, pos_tag=False):
    """
    Process a paragraph.
    Parameters:
        text: The text paragraph.
        pos_tag: Judge whether need POS tagging, False for no tag; True for tagging; default:True.
    Return: Return paragraph process result.
    """
    return NLPIR.NLPIR_ParagraphProcess(text, pos_tag)


def file_process(source_file, target_file, pos_tag=False):
    """
    Process a text file.
    Parameters:
        source_file: The source file name to be analysized;
        target_file: The result file name to store the results.
        pos_tag: Judge whether need POS tagging, False for no tag; True for tagging; default:True.
    Return: Return the processing speed if processing succeed. Otherwise return false.
    """
    return NLPIR.NLPIR_FileProcess(source_file, target_file, pos_tag)


def add_user_word(word):
    """
    Add a word to the user dictionary.
    Parameters:
        word:the word added.
    Return: Return true if add succeed. Otherwise return false.
    """
    return NLPIR.NLPIR_AddUserWord(word)


def save_user_dict():
    """
    Save the user dictionary to disk.
    Parameters: None.
    Return: Return true if add succeed. Otherwise return false.
    """
    return NLPIR.NLPIR_SaveTheUsrDic()


def delete_user_word(word):
    """
    Delete a word from the  user dictionary.
    Parameters:
        word: the word to be delete.
    Return: Return -1, the word not exist in the user dictionary; else, the handle of the word deleted
    """
    return NLPIR.NLPIR_DelUsrWord(word)


def get_keywords(text, max_limit=50, weight_out=False):
    """
    Extract keyword from paragraph.
    Parameters:
        text: the input text.
        max_limit: the maximum number of key words.
        weight_out: whether the keyword weight output or not.
    Return: Return the keywords list if excute succeed. otherwise return None.
    """
    return NLPIR.NLPIR_GetKeyWords(text, max_limit, weight_out)


def get_file_keywords(filename, max_limit=50, weight_out=False):
    """
    Extract keyword from a text file.
    Parameters:
        text: the input text filename.
        max_limit: the maximum number of key words.
        weight_out: whether the keyword weight output or not.
    Return: Return the keywords list if excute succeed. otherwise return None.
    """
    #TODO NLPIR_GetFileKeyWords exists encoding issue.
    return NLPIR.NLPIR_GetFileKeyWords(filename, max_limit, weight_out)

def get_new_words(text, max_limit=50, weight_out=False):
    """
    Extract new words from paragraph.
    Parameters:
        text: the input text.
        max_limit: the maximum number of key words.
        weight_out: whether the keyword weight output or not.
    Return: Return the keywords list if excute succeed. otherwise return None.
    """
    return NLPIR.NLPIR_GetNewWords(text, max_limit, weight_out)


def get_file_new_words(filename, max_limit=50, weight_out=False):
    """
    Extract new words from a text file.
    Parameters:
        text: the input text filename.
        max_limit: the maximum number of key words.
        weight_out: whether the keyword weight output or not.
    Return: Return the keywords list if excute succeed. otherwise return None.
    """
    #TODO NLPIR_GetFileNewWords exists encoding issue.
    return NLPIR.NLPIR_GetFileNewWords(filename, max_limit, weight_out)


def finger_print(text):
    """
    Extract a finger print from the paragraph.
    Parameters:
        text: input text.
    Return: 0, failed; else, the finger print of the content
    """
    return NLPIR.NLPIR_FingerPrint(text)


def set_POS_map(pos_map):
    """
    Select which pos map will use.
    Parameters:
        pos: POSMap
    Return: Return true if excute succeed. Otherwise return false.
    """
    return NLPIR.NLPIR_SetPOSmap(pos_map)
