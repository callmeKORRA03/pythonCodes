import numpy
mylist = [[10, 20, 30, 40], [50, 60, 70, 80]]
arr = numpy.array(mylist)

for row in arr:
    for ele in row:
        print(ele, end=' ')
