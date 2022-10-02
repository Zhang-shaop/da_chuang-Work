import numpy
list0=numpy.zeros(100)

file1 = open('E:/new dachuang/daChuangWork/data/总电压.txt', 'w')
list0.append(file1.read())
file1.close()
list0.popleft()
