# -*- coding:gbk -*-
'''ʾ��6: �Բ���������ȷ���ĺ�������װ�Σ�
������(*args, **kwargs)���Զ���Ӧ��κ���������'''


def deco(func):
    def _deco(*args, **kwargs):
        for arg in args:
            print "arg:%s" % arg
        for kwarg in kwargs:
            print "kwarg:%s" % kwarg

        print("before %s called." % func.__name__)
        ret = func(*args, **kwargs)
        print("  after %s called. result: %s" % (func.__name__, ret))
        return ret

    return _deco

@deco
def myfunc(a, b):
    print(" myfunc(%s,%s) called." % (a, b))
    return a + b

@deco
def myfunc2(a, b, c):
    print(" myfunc2(%s,%s,%s) called." % (a, b, c))
    return a + b + c


print myfunc(1, 2)
myfunc(3, 4)
print myfunc2(1, 2, 3)
myfunc2(3, 4, 5)