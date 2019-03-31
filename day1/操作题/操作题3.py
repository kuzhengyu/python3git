m = [5,8,-7,4,6,2,-3,0]

maxinum = max(m)
mininum = min(m)

#删除最小值
m.remove(mininum)

#将负数变为正数
for i in range(len(m)):
    m[i] = abs(m[i])

print("max=",maxinum,"min=",mininum,"\n",m)