'''
列表的推导和可读性：
把一个字符串变成unicode的码位列表
'''

symbols = '!@#$%^&*()'

# 方式一：
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print (codes)

# 方式二：
print([ord(symbol) for symbol in symbols])
