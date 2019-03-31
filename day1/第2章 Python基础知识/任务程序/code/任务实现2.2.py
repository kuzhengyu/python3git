# -*-coding:utf8-*-
###############################################################################
####################               正文代码                 ####################
###############################################################################
applePriceStr = 'Apple\'s unit price is 9 yuan.'
applePrice = applePriceStr[22]                                                     # 提取数值
print('提取了苹果的单价为：',applePrice,'。此刻他的数据类型为：',type(applePrice))
applePrice = int(applePrice)                                                        # 字符转数值
print('转换数据类型后：',type(applePrice))

#修改
#字符与数值互相转换
value = 10
char = '10'
value2= str(value)
char2 = int(char)
print('字符转数值',int(char),type(value2))
print('数值转字符',str(value),type(char2))

