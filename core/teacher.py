"""
老师视图
"""

def login():
    pass


def check_course():
    pass


def choose_course():
    pass


def check_stu_from_course():
    pass


def change_score_from_student():
    pass


# 老师功能字典
func_dict = {
    '1': login,
    '2': check_course,
    '3': choose_course,
    '4': check_stu_from_course,
    '5': change_score_from_student,
}

# 学生视图函数
def teacher_view():
    while True:
        print(
            '''
        - 1.登录
        - 2.查看教授课程
        - 3.选择教授课程
        - 4.查看课程下学生
        - 5.修改学生分数
            '''
        )
        choice = input('请输入老师功能编号:').strip()

        if choice == 'q':
            break

        if choice not in func_dict:
            print('编号不对请重新输入')
            continue

        func_dict.get(choice)()