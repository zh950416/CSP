'''
存放各种类
'''
from db import db_handler

# 基类
class base:
    @classmethod
    def select(cls, username):
        obj = db_handler.select_data(cls, username)
        return obj

    def save(self):
        db_handler.save_data(self)

# 管理员类
class Admin(base):

    def __init__(self,user,pwd):
        self.user = user
        self.pwd = pwd

    # 创建学校
    def creat_school(self,school_name,school_addr):
        school_obj = School(school_name,school_addr)
        school_obj.save()

    # 创建课程
    def creat_course(self,schoole_obj,course_name):
        course_obj = Course(coursr_name)
        course_obj.save()

        school_obj.course_list.append(course_name)

        schoole_obj.save()

    # 创建老师
    def creat_teacher(self, teacher_name, teacher_pwd):
        teacher_obj = Teacher(teacher_name, teacher_pwd)
        teacher_obj.save()

# 学校类

class School(base):
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.course_list = []   # 学校对应的课程


# 课程类
class Course(base):
    def __init__(self,course_name):
        self.course_name = course_name
        self.student_list = []


# 老师类

class Teacher(base):
    def __init__(self,teacher_name,teacher_pwd):
        self.user = teacher_name
        self.pwd = teacher_pwd
        self.course_list_from_tea = []

