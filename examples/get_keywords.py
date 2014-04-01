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

    text = '“屌丝”这个嘲讽意味的代词迅速爆红，迎合了大众的心理和趣味。因为你会发现从表面符合屌丝定义的人，到和屌丝属性八竿子打不着的人，都在争相认领这一名号。当人人都在忙着确认自己的屌丝身份，并乐此不疲时，屌丝一词一定与时代的什么特征实现了合拍。“屌丝”不是阿Q，他们公然比惨并乐在其中有评论认为，“屌丝”是新时代的阿Q，两者并不完全相同。首先，阿Q是文学巨匠鲁迅一己之力创造的，而“屌丝”则是网络群体狂欢的结果，它是真正由网民集体创作的形象；另外，阿Q最重要的特征是“精神胜利法”，梦想的是“银盔银甲”，意淫的是“我手持钢鞭将你打”。'
    print get_keywords(text)

    exit()
