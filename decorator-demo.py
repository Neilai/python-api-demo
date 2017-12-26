__author__ = "Neil"
__time__ = "2017/12/26 11:59"

from inspect import signature
from functools import update_wrapper,wraps
import time,logging

#例一
#装饰器的本质是一个函数调用，参数是函数的引用  f=decrotaor(f)
def memo(func):
    cache={}
    #返回包裹函数形成闭包
    def wrap(*args):
        if args not in cache:
            cache[args]=func(*args)
        return cache[args]
    return wrap

#该装饰器的作用是对于每一个相同参数的调用，都有一个缓存
#例二
def mydecorator(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        '''wrapper function'''
        print("in wrapper")
        func(*args,**kwargs)
    #update_wrapper(wrapper,func,('__name__','__doc__'),'__dict__')
    return  wrapper
@mydecorator
def example():
    '''example function'''
    print("in example")
# print(example.__name__)
# print(example.__doc__)
#闭包会导致函数元信息改变,需要调用update_wrapper  第二个参数是要更新的信息，第三个参数是要合并的信息.   也可以比较便捷的调用装饰器 wraps

#例三 带参数的装饰器，多一层包装
def typeassert(*ty_args,**ty_kargs):
    def decorator(func):
        #获取函数的元信息,绑定类型
        sig=signature(func)
        btypes=sig.bind_partial(*ty_args,**ty_kargs).arguments
        #wrapper处的是函数变量
        def wrapper(*args,**kargs):
            for name,obj in sig.bind(*args,**kargs).arguments.items():
                if name in btypes:
                    if not isinstance(obj,btypes[name]):
                        raise TypeError("%s must be %s"%(name,btypes[name]))
            return func(*args,**kargs)
        return wrapper
    return  decorator

@typeassert(int,int,int)
def f(a,b,c):
    print(a,b,c)
# f(1,2,3)
# f('1',2,3)

#例四，时间统计装饰器

def warn(timeout):
    def decorator(func):
        #wrapper对每一个实例进行处理
        def wrapper(*args,**kargs):
            start=time.time()
            res=func(*args,**kargs)
            used=time.time()-start
            if used>timeout:
                msg='"%s":%s>%s'%(func.__name__,used,timeout)
                logging.warning(msg)
            return res
        return wrapper
    return decorator

@warn(0.2)
def test():
    print('in test')
    time.sleep(1.5)
# test()