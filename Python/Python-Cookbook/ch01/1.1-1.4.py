# 现在有一个包含 N 个元素的元组或者是序列，
# 怎样将它里面的值解压后同时赋值给 N 个变量？

data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data

s = 'Hello'
a, b, c, d, e = s


# 如果一个可迭代对象的元素个数超过变量个数时，
# 会抛出一个 ValueError 。
# 那么怎样才能从这个可迭代对象中解压出 N 个元素出来？

def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)


line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')


def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head


# 在迭代操作或者其他操作的时候，怎样只保留最后有限几个元素的历史记录？
from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


# Example use on a file
if __name__ == '__main__':
    with open(r'../../cookbook/somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)

q = deque()
q.append(1)
q.append(2)
q.appendleft(4)


# 怎样从一个集合中获得最大或者最小的 N 个元素列表？
import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums)) # Prints [42, 37, 23]
print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])