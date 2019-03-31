#获取输入且转换成浮点型
n1 = float(input("n1="))
n2 = float(input("n2="))
n3 = float(input("n3="))

n = []
#append参数只能是一个
n.append(n1)
n.append(n2)
n.append(n3)


#均值
u = sum(n)/3

#平方差
xita2 = 0
s=0
for i in range(3):
    s += (n[i]-u)**2
xita2 = s/3

#标准差
import math
xita = math.sqrt(xita2)

#输出结果
print("u=",u,
      "xita2=",xita2,
        "xita=",xita)