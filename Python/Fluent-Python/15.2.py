'''
with 语句的相关操作
'''

dirpath = 'E:\\learn\\Python\\Fluent-Python\\'

with open(dirpath + '15.1.py', 'r', encoding='utf-8') as f:
    src = f.read()

print(len(src))
print(src)
