# -*- encoding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    单例模式（Singleton Pattern）是一种常用的软件设计模式，该模式的主要目的是确保某一个类只有一个实例存在。

    :copyright: (c)  2018/7/27 by zwhset.
    :license: OPS, see LICENSE_FILE for more details.
"""

"""exp 1
其实，Python 的模块就是天然的单例模式，因为模块在第一次导入时，会生成 .pyc 文件，
当第二次导入时，就会直接加载 .pyc 文件，而不会再次执行模块代码。因此，我们只需把相关的函数和数据定义在一个模块中，
就可以获得一个单例对象了。
"""
class MySingletonModule(object):
    def foo(self):
        pass

my_singleton = MySingletonModule()



"""exp 2
__new__
将类的实例和一个类变量 _instance 关联起来，如果 cls._instance 为 None 则创建实例，否则直接返回 cls._instance
"""

class MySingleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(MySingleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

"""exp 3
装饰器
定义了一个装饰器 singleton，它返回了一个内部函数 getinstance，
该函数会判断某个类是否在字典 instances 中，如果不存在则会将 cls 作为 key，
cls(*args, **kw) 作为 value 存到 instances 中，否则，直接返回 instances[cls]。

"""
from functools import wraps

def singleton(cls):
    instances = {}
    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return cls(*args, **kwargs)
    return get_instance

"""exp 4
metaclass
拦截类的创建
修改类的定义
返回修改后的类
"""

class MetaClassSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaClassSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Meta1(object):
    __metaclass__ = MetaClassSingleton
