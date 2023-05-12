#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/26 16:04
# @Author  : shucun tian
# @File    : print_result.py
# @Software: PyCharm

import pickle
import os

def PrintTopNResult(n, t_src, write_src, index2word_src):
    with open(t_src, 'rb') as file_read:
        t = pickle.load(file_read)
    with open(index2word_src, 'rb') as file_read:
        index2word = pickle.load(file_read)
        
    t = sorted(t.items(), key = lambda item:item[1], reverse=True)
    with open(write_src, 'w') as file_write:
        for i in range(n):
            s = ''

            print(t[i])
            print('->')
            print(index2word[0][t[i][0][0]].decode('utf-8'))
            print('->')
            print(index2word[1][t[i][0][1]].decode('utf-8'))
            print('----------')
            print(t[i][1])
            s = str(t[i]) + '->' + str(index2word[0][t[i][0][0]].decode('utf-8')) + '->'
            s += str(index2word[1][t[i][0][1]].decode('utf-8')) + '----------' + str(t[i][1]) + '\n'
            file_write.write(s)


if __name__ == '__main__':
    t_src = os.path.join(os.path.abspath('.'), 'result', 't.pkl')
    index2word_src = os.path.join(os.path.abspath('.'), 'result', 'index2word.pkl')
    write_src = os.path.join(os.path.abspath('.'), 'result', 'output')
    PrintTopNResult(100, t_src, write_src, index2word_src)