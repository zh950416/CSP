"""
主视图
"""
from core import admin
from core import teacher
from core import student
func_dict = {
    '1':admin.admin_view,
    '2':teacher.teacher_view,
    '3':student.student_view,
}


def run():
    while True:
        print(
            """
            1.管理员功能
            2.学生功能
            3.老师功能
            """
        )
        choice = input('请输入功能编号:').strip()

        if choice not in func_dict:
            print('编号不对请重新输入')
            continue
        func_dict.get(choice)()


