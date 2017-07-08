# -*- coding:gbk -*-
'''ʾ��7: ��ʾ��4�Ļ����ϣ���װ������������
����һʾ�������������һ���װ��
װ�κ�����ʵ����Ӧ��������Щ'''


def deco(arg):
    def _deco(func):
        def __deco():
            print("before %s called [%s]." % (func.__name__, arg))
            func()
            print("  after %s called [%s]." % (func.__name__, arg))

        return __deco

    return _deco


@deco("mymodule")
def myfunc():
    print(" myfunc() called.")


@deco("module2")
def myfunc2():
    print(" myfunc2() called.")


myfunc()
myfunc2()