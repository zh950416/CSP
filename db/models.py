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
    def create_school(self,school_name,school_addr):
        school_obj = School(school_name,school_addr)
        school_obj.save()

    # 创建课程
    def create_course(self,school_obj,course_name):
        course_obj = Course(course_name)
        course_obj.save()

        school_obj.course_list.append(course_name)
        school_obj.save()

    # 创建老师
    def create_teacher(self, teacher_name, teacher_pwd):
        teacher_obj = Teacher(teacher_name, teacher_pwd)
        teacher_obj.save()

# 学校类####
####sdsd

class School(base):
    def __init__(self,name,addr):
        self.user = name
        self.addr = addr
        self.course_list = []   # 学校对应的课程

#######
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

    def show(self, teacher_name):
        return self.course_list_from_tea

    def add_course_interface(self,course_name):
        self.course_list_from_tea.append(course_name)
        self.save()

    def get_student(self,course_name):
        course_obj = Course.select(course_name)
        return course_obj.student_list

    def show_course(self):
        return self.course_list_from_tea

    def change_score(self,course_name, student_name, score):
        student_obj = Student.select(student_name)

        # 2、再给学生对象中的课程修改分数
        student_obj.score_dict[course_name] = score
        student_obj.save()




# 学生类
class Student(base):
    def __init__(self,user, pwd):
        self.user = user
        self.pwd = pwd
        self.school = None
        self.course_list = []
        self.score_dict = {}

    def add_school(self,school_name):
        self.school = school_name
        self.save()

    def add_course(self,course_name):
        self.course_list.append(course_name)
        self.score_dict[course_name] = 0
        self.save()

        # 学生选择课程的课程里 添加学生
        course_obj = Course.select(course_name)
        course_obj.student_list.append(self.user)
        course_obj.save()

class Course(base):
    def __init__(self, course_name):
        self.user = course_name
        self.student_list = []

