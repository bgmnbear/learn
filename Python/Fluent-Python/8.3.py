'''
浅复制
'''

l1 = [1, 2, 3, [4, 5]]

l2 = list(l1)  # 通过构造方法进行复制
# l2 = l1[:]  # 也可以这样想写

l2.append(9)
print('l1: {} \nl2: {}'.format(l1, l2))

l2[3].append(8)
print('l1: {} \nl2: {}'.format(l1, l2))
