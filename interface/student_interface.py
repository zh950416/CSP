"""
# 学生视图
"""
from core import student
from db import models


# 学生注册
def student_register_interface(username,password):
    # 查看是否存在
    student_obj = models.Student.select(
        username
    )

    if student_obj:
        return False,'用户存在'
    student_obj =models.School(
        username, password
    )
    student_obj.save()
    return True,'用户注册成功'

# 选学校
def add_student_interface(school_name, student_name):
    student_obj = models.Student.select(school_name)

    if not student_obj.school:
        return False, '已经存在，重新选择'

    student_obj = add_student(student_name)
    return True, '学校选择成功'

# 选课

def get_course_list_interface(student_name):
    student_obj = models.Student.select(student_name)
    school_name = student_obj.school
    if not student_name:
        return False, '无学校'

    school_obj = models.School.select(school_name)

    course_list = school_obj.course_list
    if not course_list:
        return False, '没有课程，请先联系管理员创建'


    return True, course_list


def add_course_interface( course_name, student_name):
    # 课程是否已经存在
    student_obj = models.Student.select(student_name)

    if course_name in student_obj.course_list:
        return False, '该课程已经选择过了!'

        # 2、调用学生对象中添加课程的方法
    student_obj.add_course(course_name)

    return True, f'[{course_name}] -- 课程添加成功!'

# 学生会查看分数接口
def check_score_interface(student_name):
    student_obj = models.Student.select(student_name)
    if student_obj.score_dict:
        return student_obj.score_dict