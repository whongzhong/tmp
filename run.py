#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/26 13:23
# @Author  : shucun tian
# @File    : run.py
# @Software: PyCharm

import  pickle
from data_processing import *
from IBM_algorithm import *
import os

'''
not import NULL(origin) :431 second
import NULL (origin):435 second

not import NULL:419s
1
0.00212410092247
0.00246488671093
0.00195776723896
0.00137608143849

import NULL:418s
1
0.00211163771106
0.002450423931
0.00194627999429
0.00136800724874
'''

if __name__ == '__main__':

    print(os.path.join(os.path.abspath('..'), 'IBM-model1', 'result'))
    if not os.path.exists(os.path.join(os.path.abspath('..'), 'IBM-model1', 'result')):
        os.mkdir(os.path.join(os.path.abspath('..'), 'IBM-model1', 'result'))

    foreign_sentences_embedding, native_sentences_embedding, foreign_index_to_word, \
        native_index_to_word = RunDataProcess()
    t = Init(foreign_sentences_embedding, native_sentences_embedding)
    t = IBMAlgorithm(foreign_sentences_embedding, native_sentences_embedding, t, foreign_index_to_word\
                 , native_index_to_word)
    result_file_src = os.path.join(os.path.abspath('..'), 'IBM-model1', 'result', 't.pkl')
    with open(result_file_src, 'wb') as file_write:
        pickle.dump(t, file_write)
