"""
管理员视图
"""

from interface import admin_interface
from interface import student_interface
from interface import teacher_interface

admin_info = {
    'user':None
}


def register():
    while True:
        username = input('请输入账号:').strip()
        password = input('请输入密码:').strip()
        re_password = input('请再一次输入密码:').strip()

        if password == re_password:
            flag, msg = admin_interface.admin_register_interface(username,password)
            if flag:
                print(msg)
                break
            else:
                print(msg)

        else:
            print('两次密码不一致，请重新输入')


# 管理员登录
def login():
    while True:
        username = input('请输入账号:').strip()
        password = input('请输入密码:').strip()

    # 调用管理员登录接口
        flag, msg = admin_interface.admin_login_interface(
            username, password
        )
        if flag:
            print(msg)
            admin_info['user'] = username
            break
        else:
            print(msg)


def create_school():
    # 输入学校名称，地址，创建人也要穿减去
    while True:
        school_name = input('请输入学校名字:').strip()
        school_addr = input('请输入学校地址:').strip()
    # 调用学校类，查询学校是否存在
        flag, msg = admin_interface.create_school_interface(
            # 学校名、学校地址、创建学校的管理员
            school_name, school_addr, admin_info.get('user')
        )
        if flag:
            print(msg)
            break
        else:
            print(msg)

def create_course():
    while True:
       # 获取所有学校的信息
        flag, school_list_or_msg = common_interface.get_all_school_interface()
        if not flag:
            print(school_list_or_msg)
            break
        for index,school_name in enumerate(school_list_or_msg):
            print(f'学校编号{index}    学校名称{school_name}')
        choice = input('请输出学校编号数字：').strip()

        if not choice.isdigit():
            print('请输入数字')
            continue
        choice = int(choice)

        if choice not in range(len(school_list_or_msg)):
            print('输入正确编号')
            continue

        school_name = school_list_or_msg[choice]

        # 调用创建课程接口，管理员去创建
        flag,msg = admin_interface.create_course_interface(
            school_name, course_name ,admin_info.get('user')
        )

        if flag:
            print(msg)
            break
        else:
            print(msg)


def create_teacher():
    while True:
        teacher_name = input('请输入老师名字：').strip()

        flag,msg = teacher_interface.creat_teacher_interface(
            teacher_name,admin_info.get('user')
        )

        if flag:
            print(msg)
            break
        else:
            print(msg)



# 管理员功能字典
func_dict={
    '1': register,
    '2': login,
    '3': create_school,
    '4': create_course,
    '5': create_teacher,
}

# 管路员视图函数
def admin_view():
    while True:
        print(
            '''
            1.注册
            2.登录
            3.创建学校
            4.创建课程(先选择学校)
            5.创建讲师
            '''
        )
        choice = input('请输入管理员功能编号:').strip()

        if choice == 'q':
            break

        if choice not in func_dict:
            print('编号不对请重新输入')
            continue

        func_dict.get(choice)()
