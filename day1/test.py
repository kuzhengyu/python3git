'''
mylist1=list((1,2.0,['three','four',5],6.5,True))     # 向list( )函数传入一个元组对象
print(mylist1,type(mylist1) )     # 查看对象类型
empty_list=list()                                      # 创建空列表
print(empty_list)
mylist2=list(['one','two','three'])                    # 向list( )函数传入一个列表对象
print(mylist2)
'''

'''
for i in range(5):
    if i==4:
        break
    print(i+1)

'''

'''
for i in range(0, 3):
    if i == 1:
        print('pass块')
        pass
    print(i)
'''

'''
num = zeros(shape=(3,3))
print(num)
'''



'''
class Qcute:
    stander = 'fuyou'
    __name = 'self'     #私有化
    def __init__(self,age):
        self.age = age
    def called(self):
        print(self.__name,self.stander,self.age)

Q = Qcute(10)
Q.called()

class Qtiny(Qcute):
    def setsname(self,newname):
        self.stander = newname
q = Qtiny(12)
q.called()
q.setsname("killerQueen")
q.called()
'''
print(int(30.215))
