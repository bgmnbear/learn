'''
单词序列v1
'''

import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        # 返回一个字符串列表、元素为正则所匹配到的非重叠匹配】
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        # 返回指定索引上的单词
        return self.words[index]

    def __len__(self):
        # 完善序列的协议，我们实现len方法
        return len(self.words)

    def __repr__(self):
        # 该函数用于生成大型数据结构的简略字符串的表现形式
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        '''明确表明该类型是可以迭代的'''
        # 初始化对应的迭代器，并返回
        return SentenceIterator(self.words)


class SentenceIterator:
    def __init__(self, words):
        self.words = words  # 该迭代器实例应用单词列表
        self.index = 0  # 用于定位下一个元素

    def __next__(self):
        try:
            word = self.words[self.index]  # 返回当前的元素
        except IndexError:
            raise StopIteration()
        self.index += 1  # 索引+1
        return word  # 返回单词

    def __iter__(self):
        return self


        # TEST 该类是否能够完成迭代


s = Sentence('Ehco is a good Python coder')
print(s)
for word in s:
    print(word)
