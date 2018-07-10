import collections

ct = collections.Counter('asdfghjk')
print(ct)
ct.update('qweqweqweqwe')
print(ct)
print(ct.most_common(2))