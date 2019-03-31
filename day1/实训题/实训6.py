#24的公约数序列
a = [1,2,3,4,6,8,12,24]
#36的公约数序列
b = [1,2,3,4,6,9,12,18,36]

#两个序列的最大值和最小值
max1 = max(a)
max2 = max(b)
min1 = min(a)
min2 = min(b)

print('max1={},max2={},min1={},min2={}'.format(max1,max2,min1,min2))

#最大公约数q
set1 = set(a)
set2 = set(b)
q = max(set1&set2)

print("最大公约数",q)


#两个数的乘积等于这两个数的最大公约数与最小公倍数的积。
#最小公倍数p= 两者乘积/最大公约数
p = 24*36/q

print("最小公倍数",p)


#24与36各自独有的公约数
set3 = set1-set2
set4 = set2-set1

print("24独有公约数",set3,"36独有公约数",set4)

