# -*- encoding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    简单工厂模式
        简单工厂模式又叫静态工厂方法模式，工厂模式家族中最简单的一种模式。这个模式的基本工作方式： 通过一个工厂来决定创建哪种具体的产品实例。

    简单工厂模式的组成要素
        工厂函数
            负责具体产品对象的创建工作，是该模式的核心。当场景比较复杂时，可能需要用一个工厂类来负责产品的创建。
        产品的抽象接口或抽象类
            抽象所有产品的公共接口
        具体产品类
            抽象接口的具体实现类

    简单工厂模式的好处是可以将产品对象的细节封装在其实现类的内部，改变一个产品对象具体实现不会影响其他产品。
    可扩展性强，当需要新增产品类型时，只需要添加对应的实现类，然后修改工厂，
    增加一个判断分支即可。修改工厂函数带来的风险比较低。

    :copyright: (c)  2018/7/30 by zwhset.
    :license: OPS, see LICENSE_FILE for more details.
"""

"""Example 1"""
class Dog(object):
    pass


class Cat(object):
    pass

def create_animal(name):
    """创建动物的工厂类"""

    if name == 'dog':
        return Dog()
    elif name == 'cat':
        return Cat()

    raise ValueError('factory only sup dog and cat')

"""Example 2"""

def operator_factory(op)

    if op == '+':
        return AddOperation()
    elif op == '-':
        return SubOperation()
    elif op == '*':
        return MulOperation()
    elif op == '/':
        return DivOperation()

    return ValueError('factory only sup + - * /')