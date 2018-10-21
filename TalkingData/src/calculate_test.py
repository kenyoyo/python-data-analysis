import operator

a = {}
a[30] = [1,1]
a[20] = [2,2]
a[10] = [3,3]
a[10][0] += 5

print(a)
print(sorted(a.items(), key=operator.itemgetter(1)))