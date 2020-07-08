import operator
import struct
import sys


#
assert abs(-10) == 10
assert abs(-10.5) == 10.5


class TestClass():
    def __abs__(self):
        return 5


tt = TestClass()
assert abs(tt) == 5

#
assert all([True, True, True]) == True
assert all({True, True, True}) == True
assert all((True, True, True)) == True
assert all([True, True, False]) == False
assert all({True, True, False}) == False
assert all((True, True, False)) == False

#
assert any([True, True, True]) == True
assert any({True, True, True}) == True
assert any((True, True, True)) == True
assert any([True, True, False]) == True
assert any({True, True, False}) == True
assert any((True, True, False)) == True

#
assert ascii("a") == "'a'"
assert bin(10) == '0b1010'

assert bool(10) == True

# breakpoint()

# bytearray()??
assert bytes(5) == b'\x00\x00\x00\x00\x00'

x = 1
assert callable(x) == False
assert callable(int) == True
assert chr(97) == 'a'

# @classmethod()
# compile()???

assert complex('1+2j') + 1 == complex('2+2j')
assert complex('1+2j') + complex('0+2j') == complex('1+4j')

#


class TestClass():
    apple = 'red'


assert hasattr(TestClass, 'apple') == True
assert hasattr(TestClass, 'banana') == False

assert getattr(TestClass, 'apple') == 'red'
try:
    getattr(TestClass, 'banana')
except AttributeError:
    pass
else:
    raise Exception
#
setattr(TestClass, 'banana', 'yellow')
delattr(TestClass, 'apple')
#
assert hasattr(TestClass, 'apple') == False
assert hasattr(TestClass, 'banana') == True
try:
    getattr(TestClass, 'banana')
except AttributeError:
    raise Exception
else:
    pass

#
assert dict(k='v') == {'k': 'v'}
assert dict(zip(['k'], ['v'])) == {'k': 'v'}
assert 'unpack' in dir(struct)


class Shape():
    def __dir__(self):
        return ['a', 'b']


s = Shape()
assert dir(s) == ['a', 'b']


assert divmod(5, 3) == (1, 2)
c = ['a', 'b']
assert list(enumerate(c)) == [(0, 'a'), (1, 'b')]
x = 1
assert eval('x+1') == 2

assert exec('''
print("Hello")
''') == None

# try to filter value less than 2
iterable = {"a": 1, "b": 2, "c": 3}
function = lambda elem: elem[1] < 2
print(iterable)

result = dict(filter(function, iterable.items()))
assert result == {'a': 1}

assert float(3.5) == 3.5

from string import Template
a = "abcd"
print(f"{a!r:=^30}")
print("{!r:=^30}".format(a))
mytemp = Template("{$who are $you}")
mytemp.substitute(who='mason', you="lin")

# frozenset
import string
a=[1,2,3]
b=frozenset(a)
c=list(b)
print(c)
assert a == c

c=zip(string.ascii_lowercase[:3], b)
print(c)
d=dict(c)
print(d)

globals()

hash('a')
# help() very useful
assert hex(255) == '0xff'

a=1
id(a)

# input()
assert int(0xff) == 255
assert isinstance(100, int)

from collections import defaultdict
assert issubclass(defaultdict, dict)

# iter()
# len()
# list()
# locals()
# map()
# max()
# memoryview()
# min()
# next()
# object()
# oct()
# open()
# ord()
# pow()
# print()
# property()
# range()
# repr()
# reversed()
# round()
# set()
# slice()
# sorted()
# staticmethod()
# str()
# sum()
# super()
# tuple()
# type()
# vars()
# zip()
# __import__()

print("All PASS!")
