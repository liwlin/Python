python_versions = [1.0, 1.5, 1.6, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6]
print(python_versions[0])   
'''注意列表中的第一个元素，1.0 位于索引 0 ，而不是索引 1。
许多编程语言都遵循这个惯例，我们将其称为 \"零索引\"。
如果零索引容易混乱，请考虑此种方式：元素的索引描述元素距离列表开头的距离。第一个元素距离开头有 0 个元素，
第二个元素有一个元素，依此类推。'''


months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
q3 = months[6:8]  #切片方法：第6个元素的前方切入，第8个元素的前方切入，两个切入点的范围就是目标值
print(q3)

name = "- \n".join(months)
print(name)


def top_three(input_list):
    """Returns a list of the three largest elements input_list in order from largest to smallest.

    If input_list has fewer than three elements, return input_list element sorted largest to smallest/
    """
    # TODO: implement this function
    ipput_list = []
    sorted (input_list, reverse=True)
    input_list = input_list[:3]
    return(input_list)

print(top_three())