#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/26 13:27
# @Author  : shucun tian
# @File    : IBM_algorithm.py
# @Software: PyCharm
import pickle
import os

def Init(foreign_sentences_embedding, native_sentences_embedding):
    t = {}  #key is (native, foreign), value is number
    denominator = {} #key is (foreign), value is number
    for sentence_index in range(len(foreign_sentences_embedding)):
        for native_word in native_sentences_embedding[sentence_index]:
            #if you want to import NULL, please uncomment following lines
            # if denominator.has_key(0):
            #     denominator[0] += 1
            # else:
            #     denominator[0] = 1
            # if t.has_key((native_word, 0)):
            #     t[(native_word, 0)] += 1
            # else:
            #     t[(native_word, 0)] = 1
            for foreign_word in foreign_sentences_embedding[sentence_index]:
                if (native_word, foreign_word) in t.keys():
                    t[(native_word, foreign_word)] += 1
                else:
                    t[(native_word, foreign_word)] = 1
                if foreign_word in denominator.keys():
                    denominator[foreign_word] += 1
                else:
                    denominator[foreign_word] = 1
    for key in t.keys():
        t[key] = (1.0/denominator[key[1]])
    return t

def IBMAlgorithm(foreign_sentences_embedding, native_sentences_embedding, t, \
                 foreign_index_to_word, native_index_to_word):
    threshold = 1e-3
    avg_change = 1
    s = {} #key is native embedding, value is number
    count = {} #key is (native_embedding, foreign_embdding), value is number
    total = {} #key is foreith_embdding, value is number
    iter = 0
    while avg_change > threshold:
        with open(os.path.join(os.path.abspath('..'), 'IBM-model1', 'result', str(iter) + 't.pkl'), 'wb') as file_write:
            pickle.dump(t, file_write)
        print(avg_change)
        sum_change = 0.0
        count.clear()
        total.clear()
        for sentence_index in range(len(foreign_sentences_embedding)):
            s.clear()
            for native_word in native_sentences_embedding[sentence_index]:
                s[native_word] = 0.0
                for foreign_word in foreign_sentences_embedding[sentence_index]:
                    s[native_word] += t[(native_word, foreign_word)]
            for native_word in native_sentences_embedding[sentence_index]:
                for foreign_word in foreign_sentences_embedding[sentence_index]:
                    if (native_word, foreign_word) in count.keys():
                        count[(native_word, foreign_word)] += (t[(native_word, foreign_word)] / s[native_word])
                    else:
                        count[(native_word, foreign_word)] = (t[(native_word, foreign_word)] / s[native_word])
                    if foreign_word in total.keys():
                        total[foreign_word] += (t[(native_word, foreign_word)] / s[native_word])
                    else:
                        total[foreign_word] = (t[(native_word, foreign_word)] / s[native_word])
        for foreign_word in foreign_index_to_word:
            for native_word in native_index_to_word:
                if (native_word, foreign_word) in count.keys():
                    new_t = count[(native_word, foreign_word)] / total[foreign_word]
                    sum_change += abs(new_t - t[(native_word, foreign_word)])
                    t[(native_word, foreign_word)] = new_t
        avg_change = sum_change / len(t)
        iter += 1
    return t


