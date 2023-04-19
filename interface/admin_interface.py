"""
管理员接口
"""
from db import models


def admin_register_interface(username, password):
    # 验证是否存在
    # 调用类管理文件中的admin类.select方法
    admin_obj = models.Admin.select(
        username
    )
    # 存在，创建失败
    if admin_obj:
        return False, '用户已存在！'

    # 不存在，则创建
    admin_obj = models.Admin(
        username, password
    )
    admin_obj.save()
    return True, '用户注册成功！'

# 登录接口
def admin_login_interface(username, password):
    # 验证文件是否存在。
    admin_obj = models.Admin.select(username)

    if not admin_obj:
        return False, '用户不存在'

    if password == admin_obj.pwd:
        return True, '用户登陆成功！'
    else:
        return False, '密码错误'

# 学校创建接口
def create_school_interface(school_name, school_addr, admin_name):
    # 查看学校是否存在
    school_obj = models.School.select(school_name)

    # 如果不空创建
    if school_obj:
        return False, '学校已经存在'


    # 如果为空，由管理员创建，并传入地址和名称
    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_school(
        school_name, school_addr
    )
    return True, '学校创建成功'

# 创建老师接口
def creat_teacher_interface(teacher_name,admin_name,teacher_pwd='123'):
    teacher_obj = models.Teacher.select(teacher_name)

    if teacher_obj:
        return False,'老师已经存在'

    # 若不存在
    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_teacher(teacher_name,teacher_pwd)

    return  True ,f'[{teacher_name}]老师创建成功'


