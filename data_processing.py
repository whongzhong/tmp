#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/26 13:27
# @Author  : shucun tian
# @File    : data_processing.py
# @Software: PyCharm

import os
import sys
import pickle



def ReadData(file_src):
    with open(file_src, 'rb') as file_read:
        l = file_read.readlines()
    return l

def Word2Index(sentences):
    '''
    translate word to embedding
    and the vacabulary is all words appeared in data 
    '''
    word_to_index = {}  #{key is word, value is index} like{'the':100}
    index_to_word = {}  #{key is index, value is word} like{100:'the'}
    #count is the initialization of index
    count = 0 
    #if you want to import Null, please initialize count as 1 and uncomment following lines, otherwise set count as 0
    # word_to_index['NULL'] = 0
    # index_to_word[0] = 'NULL'
    # count = 1
    for sentence in sentences:
        for word in sentence.split():
            if not word.lower() in word_to_index:
                #i translate the word to its lowercase
                word_to_index[word.lower()] = count
                index_to_word[count] = word.lower()
                count += 1
    return word_to_index, index_to_word

def Sentence2Embedding(sentences, word_to_index):
    '''
    translate sentence to vector using word embedding
    '''
    result = []
    for sentence in sentences:
        temp = []
        for word in sentence.split():
            temp.append(word_to_index[word.lower()])
        result.append(temp)
    return result

def RunDataProcess():
    foreign_file_src = os.path.join(os.path.abspath('..'), 'IBM-model1', 'data', 'fr.txt')
    foreign_sentences = ReadData(foreign_file_src)
    foreign_word_to_index, foreign_index_to_word = Word2Index(foreign_sentences)
    # print len(foreign_word_to_index)  # 14154
    foreign_sentences_embedding = Sentence2Embedding(foreign_sentences, foreign_word_to_index)
    native_file_src = os.path.join(os.path.abspath('..'), 'IBM-model1', 'data', 'en.txt')
    native_sentences = ReadData(native_file_src)
    # print native_sentences[0].decode('utf-8')  #ouput is chinses ,so we need to decode
    native_word_to_index, native_index_to_word = Word2Index(native_sentences)
    # print len(native_word_to_index)  #17011
    native_sentences_embedding = Sentence2Embedding(native_sentences, native_word_to_index)
    index_to_word_src = os.path.join(os.path.abspath('..'), 'IBM-model1', 'result', 'index2word.pkl')
    with open(index_to_word_src, 'wb') as file_write:
        pickle.dump((native_index_to_word, foreign_index_to_word), file_write)
    return foreign_sentences_embedding, native_sentences_embedding, \
           foreign_index_to_word, native_index_to_word



