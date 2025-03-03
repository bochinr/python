import os

# 读取正常邮件的文件名列表
normalList = os.listdir('item5-ss-data/normal/')
print(normalList)

# 读取垃圾邮件的文件名列表
spamList = os.listdir("item5-ss-data/spam/")
print(spamList)

stopList = []
for line in open('item5-ss-data/stopwords.txt', encoding='utf-8'):
    stopList.append(line[:len(line) - 1])
print(stopList)

from jieba import cut
from re import sub
from collections import Counter
from itertools import chain
import numpy as np

allwordList = []  # allwordList用来存放所有邮件的内容

# 正常邮件的内容处理
for file in normalList:  # 读取正常邮件的文件名
    normalListFile = ('item5-ss-data/normal/' + file)  # normalListFile用来存放正常邮件完整的路径
    wordList = []  # 用于存放每封邮件的内容
    for line in open(normalListFile, encoding='utf-8'):  # 每次打开一封邮件并读取内容
        # 对数据进行处理
        line.strip()
        line = sub(r'[.【】0-9，。/]', '', line)  # 去除内容中的中文符号和数字
        line = cut(line)  # 对内容进行分词
        # 过滤字数小于1的词
        line = filter(lambda word: len(word) > 1, line)
        wordList.extend(line)
    words = []  # words列表用于存放过滤停用词后的每封邮件的内容
    for i in wordList:
        if i not in stopList and i.strip() != '' and i != '':
            words.append(i)
    allwordList.append(words)

# 垃圾邮件的内容处理
for file in spamList:  # 读取正常邮件的文件名
    spamListFile = ('item5-ss-data/spam/' + file)  # spamListFile用来存放正常邮件完整的路径
    wordList = []  # 用于存放每封邮件的内容
    for line in open(spamListFile, encoding='utf-8'):  # 每次打开一封邮件并读取内容
        # 对数据进行处理
        line.strip()
        line = sub(r'[.【】0-9，。/]', '', line)  # 去除内容中的中文符号和数字
        line = cut(line)  # 对内容进行分词
        # 过滤字数小于1的词
        line = filter(lambda word: len(word) > 1, line)
        wordList.extend(line)
    words = []  # words列表用于存放过滤停用词后的每封邮件的内容
    for i in wordList:
        if i not in stopList and i.strip() != '' and i != '':
            words.append(i)
    allwordList.append(words)

# 提取训练集中出现频率最高的十个词
frep = Counter(chain(*allwordList))
topTen = frep.most_common(10)
topWords = []
for i in topTen:
    topWords.append(i[0])

# 计算每个高频词在每封邮件出现的次数
vector = []
for i in allwordList:
    temp = list(map(lambda x: i.count(x), topWords))
    vector.append(temp)
vector = np.array(vector)
print(vector)

# 导入贝叶斯模块
from sklearn.naive_bayes import MultinomialNB

# 1表示正常邮件，0表示垃圾邮件
y = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
x = vector

# 创建模型并训练
model = MultinomialNB()
model.fit(x, y)

testList = os.listdir('item5-ss-data/test/')
print(testList)

# 测试邮件的内容处理
for file in testList:  # 读取正常邮件的文件名
    print(type(file))
    testListFile = ('item5-ss-data/test/' + file)  # 用来存放正常邮件完整的路径
    # print(testListFile)
    wordList = []  # 用于存放每封邮件的内容
    for line in open(testListFile, encoding='utf-8'):  # 每次打开一封邮件并读取内容
        # # 对数据进行处理
        # line.strip()
        # line = sub(r'[.【】0-9，。/]', '', line) # 去除内容中的中文符号和数字
        # line = cut(line) # 对内容进行分词
        # # 过滤字数小于1的词
        # line = filter(lambda word:len(word) > 1, line)
        wordList.extend(line)
    # print(wordList)
    words = []  # words列表用于存放过滤停用词后的每封邮件的内容
    for i in wordList:
        if i not in stopList and i.strip() != '' and i != '':
            words.append(i)
    testList.append(words)
# print(testList)

# 提取测试集中出现频率最高的十个词
frep2 = Counter(chain(*testList))
topTen2 = frep.most_common(10)
topWords2 = []
for i in topTen2:
    topWords2.append(i[0])

# 计算每个高频词在每封邮件出现的次数
vector2 = []
for i in testList:
    temp = list(map(lambda x: i.count(x), topWords2))
    vector2.append(temp)
vector2 = np.array(vector2)
print(vector2)





