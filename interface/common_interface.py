'''
公共接口
'''
import os
from conf import settings
from db import models
# 获取所有学校
def get_all_school_interface():
    school_dir = os.path.join(
        settings.DB_PATH,'School'
    )
    if not os.path.exists(school_dir):
        return False,'无学校，请联系管理员'

    school_list = os.listdir(school_dir)
    return True, school_list

# 公共登录接口
def login_interface(username, password, user_type):
    # 验证文件是否存在。
    if user_type == 'admin':
        obj = models.Admin.select(username)

    elif user_type == 'student':
        obj = models.Student.select(username)

    elif user_type == 'teacher':
        obj = models.Teacher.select(username)

    else:
        return False, '角色不存在'

    if not obj:
        return False, '用户不存在'

    if password == obj.pwd:
        return True, '用户登陆成功！'
    else:
        return False, '密码错误'