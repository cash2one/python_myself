import urllib2

# ,  timeout=5
response = urllib2.urlopen("http://bj.lianjia.com/chengjiao/101101135976.html")
print response.read()

# response.read