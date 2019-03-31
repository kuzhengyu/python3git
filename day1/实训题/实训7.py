import random

#生成随机数
number = random.randint(0,200)

#所猜次数
count = 0

#判断输入是否为数值
def isdigit(x):
    try:
        x = int(x)
        return True
    except:
        print("输入的内容不为整数")
        return False

#程序主体
print("请输入一个整数进行猜测：")
while 1:
    guess = input()

    if isdigit(guess) :                       #判断输入是否为数字
        guess = int(guess)                   #将guess转换为整数

        #判断guess大小
        if guess>number:
            print("输入大于number\n")
        elif guess<number:
            print("输入小于number\n")
        else:
            print("你猜对了！\n")
            count+=1
            break
        count+=1

print("所猜的数字为",guess,"一共猜了",count,"次")

