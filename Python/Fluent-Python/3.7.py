from types import MappingProxyType

# 元组里的第二个元素其实是一个列表的引用。
test1 = ('a', [1, 2, 3])
test1[1].append(2)
print(test1)

# 不可变映射类型：
d = {1: 'A'}
d_proxy = MappingProxyType(d)
print(d_proxy)
d_proxy[1] = 'B'
print(d_proxy)
