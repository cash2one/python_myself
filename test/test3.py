#-*- coding: UTF-8 -*-

class Test:
    '''
    this is a test demo class

    '''
    name = "sunxiang"
    __zge = 20
    def __init__(self):
        print "父类"
        # self.name = name

    def hello(self):
        '''
        say hello
        :param name:
        :return:
        '''
        print "name="+self.name

    def parentMethod(self):
        print "调用父方法"

class child(Test):
    def __init__(self):
        print "子类构造方法"

    def childMethod(self):
        print "调用子方法 child method"
