"""
学生视图
"""


def register():
    pass


def login():
    pass


def choice_school():
    pass


def choice_course():
    pass


def check_score():
    pass


# 学生功能字典
func_dict = {
    '1': register,
    '2': login,
    '3': choice_school,
    '4': choice_course,
    '5': check_score,
}

# 学生视图函数
def student_view():
    while True:
        print(
            '''
        - 1.注册
        - 2.登录功能
        - 3.选择校区
        - 4.选择课程
        - 5.查看分数
            '''
        )
        choice = input('请输入学生功能编号:').strip()

        if choice == 'q':
            break

        if choice not in func_dict:
            print('编号不对请重新输入')
            continue

        func_dict.get(choice)()