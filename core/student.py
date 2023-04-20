"""
学生视图
"""
from lib import common
from interface import student_interface
from interface import common_interface
student_info = {
    'user':None
}

# 学生注册
def register():
    while True:
        username = input('请输入账号:').strip()
        password = input('请输入密码:').strip()
        re_password = input('请再一次输入密码:').strip()

        if password == re_password:
            flag, msg = student_interface.student_register_interface(username,password)
            if flag:
                print(msg)
                break
            else:
                print(msg)

        else:
            print('两次密码不一致，请重新输入')


def login():
    while True:
        username = input('请输入账号:').strip()
        password = input('请输入密码:').strip()

    # 调用管理员登录接口
        flag, msg = common_interface.login_interface( username, password, user_type='student')
        if flag:
            print(msg)
            student_info['user'] = username
            break
        else:
            print(msg)

# 选择学校
@common.auth('student')
def choice_school():
    while True:
    # 首先展示学校并打印
        flag, school_list = common_interface.get_all_school_interface()
        if not flag:
            print(school_list)
        for index, school_name in enumerate(school_list):
            print(f'学校编号{index} 学校名称{school_name}')

        # 选择学校
        choice = input('请输入学校编号:').strip()

        choice = int(choice)

        if choice not in range(len(school_list)):
            print('编号有问题')
            continue

        school_name = school_list[choice]

        # 调用接口，查看类

        flag, msg = student_interface.add_school_interface(
        school_name, student_info.get('user')
        )

        if flag:
            print(msg)
            break

        else:
            print(msg)
            break


# 选择课程
@common.auth('student')
def choice_course():
    while True:
    # 调用接口，查看属于什么学校，学校里面有什么课程，在选课
        flag, course_list = student_interface.get_course_list_interface(student_info.get('user'))

        if not flag:
            print('course_list')
            break

        # 打印课程 然后选择
        for index, course_name in enumerate(course_list):
            print(f'课程编号{index} 课程名字{course_name}')

        choice = input('输入课程编号：').strip()
        choice = int(choice)

        if choice not in range(len(course_list)):
            print('输入编号有问题')
            choice

        course_name = course_list[choice]

        # 调用学生选课系统

        flag, msg = student_interface.add_course_interface(
            course_name, student_info.get('user')
        )

        if flag:
            print(msg)
            break
        else:
            print(msg)




    pass

# 查看分数
@common.auth('student')
def check_score():
    score_dict = student_interface.check_score_interface(
        student_info.get('user')
    )

    if not score_dict:
        print('没有选择课程!')

    print(score_dict)


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