import pandas as pd
import matplotlib.pyplot as plt

url = 'http://s3.amazonaws.com/assets.datacamp.com/course/dasi/present.txt'
present = pd.read_table(url, sep=' ')
print present.shape
print present.columns

present_year = present.set_index('year')
print present_year['boys'].plot()
print present_year.plot()
print present_year[:10].plot(kind='bar')
plt.show()
plt.legend(loc='best')
plt.savefig("test.png")


# present_year = present.set_index('year')
#
# present_year['boys'].plot()
# # plt.legend(loc='best')
#
# present_year.plot()
#
#
# present_year.girls.plot(color='g')
# present_year.boys.plot(color='b')
# plt.legend(loc='best')

# url_2 = 'https://raw.github.com/pydata/pandas/master/pandas/tests/data/iris.csv'
# iris = pd.read_csv(url_2)
# print iris.head(5)