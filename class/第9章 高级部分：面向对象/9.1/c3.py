# 类是现实世界或思维世界中的实体在计算机中的反映，它将数据以及在数据上的操作封装在一起

name = 'xx'

class Student():  #class的命名头字母一般大写
    name = ''  #数据成员，类中的变量，它刻画了数据的 特征
    age = 0
    #'类变量'；'实例（对象关联）变量'
    def __init__(self,name,age):  # 构造函数  构造函数的调用是自动的。只能返回none值
        #构造函
        # 初始化对象的属性
        self.name = name
        self.age = age
        #print('student')

    #行为 与 特征
    def do_homework(self):
        print('homework')

student1 = Student('lilei',14)
print('name:'+ student1.name +',age:' + str(student1.age))
student2 = Student('hanmeimei',15)
print('name:'+ student2.name +',age:' + str(student2.age))




#类就像是一个模板，通过类（模板）可以产生很多个不同的对象（通过不同的参数产生不同的对象）。