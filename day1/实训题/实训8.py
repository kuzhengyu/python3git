intCount = 0
strCount = 0
otherCount = 0

str = input("输入需要统计的字符串")

for i in range(len(str)):
    if str[i].isdigit():
        intCount+=1
    elif str[i].isalpha():
        strCount+=1
    else:
        otherCount+=1

print("intCount = %d , strCount = %d, otherCount = %d"% (intCount ,strCount,otherCount))


