# -*- coding: utf-8 -*-

class Classname(object):

    def __init__(self):
        self.aa = 1
        pass

    def add_sx(self, a, b):
        print self.aa
        print a + b

    def teat(self):
        print "ss"
        print self.aa

    def test_with(self):
        with open("b.txt", "rb") as f:
            content = f.read()
            print content

if __name__ == '__main__':
    test = Classname()
    test.test_with()
