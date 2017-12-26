__author__ = "Neil"
__time__ = "2017/12/26 14:51"

from inspect import signature

def f(a,b,c):
    pass

sig=signature(f)
a=sig.parameters['a']
#建立参数映射
bargs=sig.bind(int,str,str)
#也可以部分绑定
#bargs=sig.bind_partial(int,str)

print(sig.parameters)
print(a.kind)
print(a.default)
print(bargs)
#得到映射字典
print(bargs.arguments)