# 老师接口
from db import models
def check_course_interface(teacher_name):
    teacher_obj = models.Teacher.select(teacher_name)
    course_list = teacher_obj.show(teacher_name)
    if course_list:
        return True, course_list
    else:
        return False, '老师暂且还没有选课'

def add_course_interface(course_name,teacher_name):
    teacher_obj = models.Teacher.select(teacher_name)
    course_list = teacher_obj.course_list_from_tea
    if course_name in course_list:
        return False,'课程存在'

    teacher_obj.add_course_interface(course_name)

    return True, '添加课程成功!'

# 查看课程下的学生
def get_student_interface(course_name, teacher_name):
    teacher_obj = models.Teacher.select(teacher_name)

    student_list = teacher_obj.get_student(course_name)

    if not student_list:
        return False, '学生没有选择该课程'

    return True, student_list

# 查看所有课程
def check_course_interface(teacher_name):
    teacher_obj = models.Teacher.select(teacher_name)

    course_list = teacher_obj.show_course()

    if not course_list:
        return False, '老师没有选择课程'

    return True, course_list

# 获取课程下所有学生
def get_student_interface(course_name, teacher_name):
    teacher_obj = models.Teacher.select(teacher_name)

    # 2、让当前老师对象，调用获取课程下所有学生功能
    student_list = teacher_obj.get_student(course_name)

    # 3、判断课程下是否有学生
    if not student_list:
        return False, '学生没有选择该课程'

    return True, student_list
def change_score_interface(course_name, student_name,score, teacher_name ):
    teacher_obj = models.Teacher.select(teacher_name)

    # 2、让老师对象调用修改分数方法
    teacher_obj.change_score(course_name, student_name, score)

    return True, '修改分数成功！'


