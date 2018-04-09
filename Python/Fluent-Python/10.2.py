'''
多维向量类 v1
'''
import functools
import numbers
import operator
from array import array
import reprlib
import math

import itertools


class Vector:
    typecode = 'd'
    shortcut_names = 'xyzt'

    def __init__(self, components):
        # 用 _ 代表受保护的属性，把Vector的分量保存在一个数组之中
        self._components = array(self.typecode, components)

    def __iter__(self):
        # 通过_components 来构造一个迭代器
        return iter(self._components)

    def __repr__(self):
        # 使用reprlib.repr()函数来获取分量的有限长度的表现形式（防止出现1000维度的实例显示问题）
        components = reprlib.repr(self._components)
        # 通过字符串生成实例时删掉 [ 之前和 array(d) 后面的
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        # 这里我们可以直接使用_components 来构建bytes对象
        return (bytes([ord(self.typecode)]) + bytes(self._components))

    def __eq__(self, other):
        return (len(self) == len(other)) and all(a == b for a, b in zip(self, other))

    def __hash__(self):
        # 先用生成器表达式惰性计算各个分量的散列值
        hashes = (hash(x) for x in self)
        # 再用过operator的xor函数计算聚合的散列值 第三个参数0是初始值
        return functools.reduce(operator.xor, hashes, 0)

    def __abs__(self):
        # 通过计算各个分量的平方和来算出绝对值（距离）
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)  # 获取实例的类型
        if isinstance(index, slice):  # 如果index参数值是切片的对象
            # 调用Vector的构造方法，建立一个新的切片后的Vector类
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):  # 如果参数是整数类型
            return self._components[index]  # 我们就对数组进行切片
        else:  # 否则我们就抛出异常
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))

    def __getattr__(self, name):
        cls = type(self)  # 获取类型
        if len(name) == 1:  # 判断属性名是否在我们定义的names中
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self._components):
                return self._components[pos]
        msg = '{} objects has no attribute {}'
        raise AttributeError(msg.format(cls, name))

    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:  # 我们需要特别处理单个属性名的情况
            if name in cls.shortcut_names:
                error = 'readonly attrbute {}'  # 当用户想要重置xyzt的值时，抛出异常】
            elif name.islower():  # 我们不想让向量存在其他小写字母的属性
                error = "can't set attributes 'a' to 'z' in  {} "
            else:
                error = ''

            if error:
                msg = error.format(cls.__name__, name)
                raise AttributeError(msg)
        super().__setattr__(name, value)  # 没有特殊情况我们调用超类的setattr来动态增加属性

    def angle(self, n):
        # 使用 n维度球体 中的公式计算某个角坐标
        r = math.sqrt(sum(x * x for x in self[n:]))
        a = math.atan2(r, self[n - 1])
        if (n == len(self)) and (self[-1] < 0):
            return math.pi * 2 - a
        else:
            return a

    def angles(self):
        # 生成器表达式，计算所有的叫坐标
        return (self.angle(n) for n in range(1, len(self)))

    def __format__(self, fmt_spec):
        if fmt_spec.endswith('h'):  # 超球面坐标
            fmt_spec = fmt_spec[:-1]
            # 使用itertools.chain生成器表达式，无迭代向量的模和各个角坐标
            coords = itertools.chain([abs(self)], self.angles())
            out_fmt = '<{}>'  # 球面坐标
        else:
            coords = self
            out_fmt = '({})'  # 笛卡尔坐标
        components = (format(c, fmt_spec) for c in coords)  # 格式化各个元素
        return out_fmt.format(', '.join(components))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        # 直接将memv传给class即可，不用拆包
        return cls(memv)


if __name__ == '__main__':
    test = Vector([3, 4, 5])
    print(test[-1])
    print(test[:2])

    print(test.x)
    test.A = 1
    test.A = 2

    print(test.A)
    print(test)

    print(hash(test))

    test1 = Vector([3.0, 4.0, 5.0])
    print(test == test1)

    v1 = Vector([1, 1, 2])
    v2 = Vector([1, 2, 3, 4, 5, 6])
    print(format(v1, '.3f'))
    print(format(v2, '.3h'))
