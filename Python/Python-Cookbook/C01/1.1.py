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
