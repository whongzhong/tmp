import pickle

file_t= open("result/t.pkl", 'rb')
file_index2word = open("result/index2word.pkl", 'rb')
t = pickle.load(file_t)
index2word = pickle.load(file_index2word)
dict_map = {}

word_sort = sorted(t.items(), key=lambda item:item[1], reverse=True)
word_list = []
for i in range(1000):
    word_list.append(word_sort[i][0])
for i in range(1,11):
    pair = word_list[i]
    native = str(index2word[0][pair[0]],encoding='utf8')
    predict = str(index2word[1][pair[1]],encoding='utf8')
    if native[-1] == ',':
        native = native[:-1]
    if predict[-1] == ',':
        predict = predict[:-1]
    print("{:15}{:15}{:15}".format(native,predict,t[pair]))