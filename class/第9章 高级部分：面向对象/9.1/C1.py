# 面向对象
# 有意义的面向对象的代码
# 类 = 面向对象
# 类、对象 
# 实例化：要是用类必须先实例化
# 类最基本作用是封装：变量和函数

class Student():  #class的命名头字母一般大写
    name = ''  #数据成员，类中的变量，它刻画了数据的 特征
    age = 0
     #行为 用方法来表示行为  
    def print_file(self):  #方法  在类下创建函数和其他普通情况创建函数有区别，需要强制在函数的参数内加入固定关键字"self"
        print('name:' + self.name)
        print('age:' + str(self.age))



# student =Student()
# student.print_file()