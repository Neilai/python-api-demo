__author__ = "Neil"
__time__ = "2017/12/26 12:23"
#参考知乎https://www.zhihu.com/question/53536750
a = 10
b = 10
print(a is b)

a = 10.0
b = 10.0
print(a is b)

a = 10
def f():
    return 10

print(f() is a)

#小整数具有缓存机制

a = 1000
def f():
    return 1000

print(f() is a)

a = 10.0
def f():
    return 10.0
print(f() is a)
