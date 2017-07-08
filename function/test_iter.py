

sxdict = {"a":1, "b":2}
for i, v in sxdict.iteritems():
    print i, v

for v in sxdict.itervalues():
    print v

sxlist = ["1", "2", "sx"]
for a, b in enumerate(sxlist):
    print a, b