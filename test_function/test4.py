# -*- coding:gbk -*-
'''ʾ��4: ʹ����Ƕ��װ������ȷ��ÿ���º����������ã�
��Ƕ��װ�������βκͷ���ֵ��ԭ������ͬ��װ�κ���������Ƕ��װ��������'''

def deco(func):
    def _deco():
        print("before myfunc() called.")
        sx = func()
        # if sx == "ok":
        #     print "oook"
        print("  after myfunc() called.")
        # ����Ҫ����func��ʵ����Ӧ����ԭ�����ķ���ֵ

        return sx
    return _deco

@deco
def myfunc():
    print(" myfunc() called.")
    return "12345"

print myfunc()