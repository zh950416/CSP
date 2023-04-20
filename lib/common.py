"""
公共类
e"""
# 多用户认证装饰器
def auth(role):
    """
    :param role:    角色：管理员、学生、老师
    :return:
    """
    from core import admin, student, teacher
    def login_auth(fun):
        def inner(*args,**kwargs):
            if role == 'admin':
                if admin.admin_info['user']:
                    res = fun(*args, **kwargs)
                    return res
                else:
                    admin.login()
            elif role == 'student':
                if student.student_info['user']:
                    res = fun(*args, **kwargs)
                    return res
                else:
                    student.login()
            elif role == 'teacher':
                if student.teacher_info['user']:
                    res = fun(*args, **kwargs)
                    return res
                else:
                    teacher.login()
            else:
                print('当前视图没有权限')
        return inner
    return login_auth



