

print 'hello {0} i am {1} . my name is {0}'.format('Kevin', 'Tom') # hello Kevin i am Tom . my name is Kevin

print 'hello {name1}  i am {name2}'.format(name1='Kevin', name2='Tom')

names=['Kevin', 'Tom']
print 'hello {names[0]}  i am {names[1]}'.format(names=names)                  # hello Kevin i am Tom
print 'hello {0[0]}  i am {0[1]}'.format(names)

names={'name':'Kevin','name2':'Tom'}
print 'hello {names[name]}  i am {names[name2]}'.format(names=names)

class Names():
    name1 = 'Kevin'
    name2 = 'Tom'

print 'hello {names.name1}  i am {names.name2}'.format(names=Names)

args=['lu']
kwargs = {'name1': 'Kevin', 'name2': 'Tom'}
print 'hello {name1} {} i am {name2}'.format(*args, **kwargs)  # hello Kevin i am Tom

f = 'hello {0} i am {1}'.format
print f('Kevin','Tom')

print 'hello {0:>{1}} '.format('Kevin',50)


print 'hello {0}  i am {1}'.format("ssdd", 111)

zhishu = {"brand_1": 1, "brand_2": 2, "company_1": 3, "company_2": 4}
print ";brand_{zhishu[brand_1]}_1;brand_{zhishu[brand_1]}_2;company_{zhishu[company_1]}_1;company_{zhishu[company_1]}_2".format(zhishu=zhishu)

print "ext_type:{0};url:{1};headers:{2};config:{3}".format(2, "dhdh",{"js": "dkdk"}, {"dkdk": 24})