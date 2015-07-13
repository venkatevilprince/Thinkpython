import csv
b = open('test.csv', 'w')
a = csv.writer(b)
data = ['Me', 'You']
a.writerow(data),
a.writerow(data)
b.close()

x=[['a']]

print x[0][0]
