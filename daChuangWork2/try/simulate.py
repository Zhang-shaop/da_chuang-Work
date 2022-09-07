import random
import time

while True:
    file1 = open('E:/new dachuang/daChuangWork2/server-data/总电压.txt', 'w')
    file1.write(format(100*random.random(),'.2f'))
    file1.close()

    file2 = open('E:/new dachuang/daChuangWork2/server-data/总电流.txt', 'w')
    file2.write(format(100 * random.random(), '.2f'))
    file2.close()

    file3 = open('E:/new dachuang/daChuangWork2/server-data/氢槽温度.txt', 'w')
    file3.write(format(100 * random.random(), '.2f'))
    file3.close()

    file4 = open('E:/new dachuang/daChuangWork2/server-data/氧槽温度.txt', 'w')
    file4.write(format(100 * random.random(), '.2f'))
    file4.close()

    file5 = open('E:/new dachuang/daChuangWork2/server-data/碱液流量.txt', 'w')
    file5.write(format(100 * random.random(), '.2f'))
    file5.close()

    file6 = open('E:/new dachuang/daChuangWork2/server-data/碱液温度.txt', 'w')
    file6.write(format(100 * random.random(), '.2f'))
    file6.close()

    file7 = open('E:/new dachuang/daChuangWork2/server-data/1室电压.txt', 'w')
    file7.write(format(100 * random.random(), '.2f'))
    file7.close()

    file8 = open('E:/new dachuang/daChuangWork2/server-data/2室电压.txt', 'w')
    file8.write(format(100 * random.random(), '.2f'))
    file8.close()

    file9 = open('E:/new dachuang/daChuangWork2/server-data/3室电压.txt', 'w')
    file9.write(format(100 * random.random(), '.2f'))
    file9.close()

    file10 = open('E:/new dachuang/daChuangWork2/server-data/4室电压.txt', 'w')
    file10.write(format(100 * random.random(), '.2f'))
    file10.close()

    file11 = open('E:/new dachuang/daChuangWork2/server-data/5室电压.txt', 'w')
    file11.write(format(100 * random.random(), '.2f'))
    file11.close()

    file12 = open('E:/new dachuang/daChuangWork2/server-data/6室电压.txt', 'w')
    file12.write(format(100 * random.random(), '.2f'))
    file12.close()

    print('have upgraded server-data!')
    time.sleep(10)