# x = "2004/01/01 09:00:24.50,35.59900,-117.62750,8.600,3.05,Md,12,172,57,0.09,NCSN,21328352"
# x.split(",", 12)
# print x
# print x[0]


from numpy import *

file1 = genfromtxt('coordtest.txt', delimiter=",")
print file1