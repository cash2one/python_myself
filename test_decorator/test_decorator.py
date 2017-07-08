# -*- coding:utf-8 -*-


# sx_temp = "11"
# print isinstance(sx_temp, str)

def dec(func):
    def in_dec(*args):
        if len(args) == 0:
            return 0
        for arg in args:
            print arg
            if isinstance(arg, dict):
                print "dict:",arg["sx"]
            if not isinstance(arg, int):
                return 0

        sx = func(*args)
        return sx
    return in_dec

@dec
def my_sum(*args):
    return sum(args)

@dec
def my_average(*args):
    return sum(args)/len(args)

print my_sum(1,2,3, {"sx": 1})
print my_average(1,2,4)