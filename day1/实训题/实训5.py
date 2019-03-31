#通信录
m = {"小明":"001,广州",
     "小红":"002,深圳",
     "小王":"003,北京"}

#选择函数
def menu(sel):
    #添加好友功能
    if sel==1:
        input1 = input("输入姓名，其手机号码及其居住城市：（如：小明,12312,深圳）")
        message = input1.split(",",1)   #以第一个逗号作为分割点  得到message[0]是姓名  message[1]是手机和居住信息
        m[message[0]] = message[1]      #将分割的手机和居住信息存入字典
        print("添加成功")

    #删除好友
    elif sel==2:
        name = input("输入要删除的姓名：")
        if m.__contains__(name):
            del m[name]
            print("删除成功")
        else:
            print("通讯录中没有该好友")

    #修改好友信息
    elif sel==3:
        name = input("输入要修改的好友名称：")
        if m.__contains__(name):
            i = input("输入修改的手机号码及其居住城市：（如：123，广州）")
            m[name] =i
        else:
            print("通讯录中没有该好友")

    #查询好友
    elif sel ==4:
        name = input("输入要查询的好友名称：")
        if m.__contains__(name):
            print(name ,m[name])
        else:
            print("通讯录中没有该好友")

    #显示通信录
    elif sel ==5:
        print(m)

    else:
        print("输入数字有误")

def show():
    return int(input("1.添加好友\n"
              "2.删除好友\n"
              "3.好友信息修改\n"
              "4.好友信息查询\n"
              "5.显示通信录\n"
              "输入数字:"))

#菜单
while 1:
    sel = show()
    menu(sel)
