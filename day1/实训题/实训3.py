#初始化列表
fib = [0,1]

#指定长度
length = int(input("输入指定长度"))

#计算到指定长度的每一项fib数列
for i in range(2,length):
    n = fib[i-1]+fib[i-2]
    fib.append(n)

#第三项是重复项，删除
fib.pop(2)

#fib每项求和，并添加至fib末尾处
s = sum(fib)
fib.append(s)

#打印结果
print(fib)