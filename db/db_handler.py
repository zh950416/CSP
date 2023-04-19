"""
用于保存和获取对象
"""
import os
import pickle
from conf import settings

def select_data(cls,username):
    # 获取类名
    class_name = cls.__name__

    # 类文件夹路径
    user_dir_path = os.path.join(
        settings.DB_PATH,class_name
    )
    # 判断文件夹是否存在，不存在则创建
    if not os.path.exists(user_dir_path):
        os.mkdir(user_dir_path)
    # 拼接用户文件夹
    user_path = os.path.join(
        user_dir_path,username
    )

    # 判断是否存在
    if os.path.exists(user_path):
        with open(user_path,'rb')  as f:
            obj = pickle.load(f)
            return obj





def save_data(obj):
    # 获取类名
    class_name = obj.__class__.__name__
    user_dir_path = os.path.join(
        settings.DB_PATH,class_name
    )
    # 判断文件夹是否存在，不存在则创建
    if not os.path.exists(user_dir_path):
        os.mkdir(user_dir_path)

    # 拼接用户文件夹
    user_path = os.path.join(
        user_dir_path, obj.user
    )

    with open( user_path,'wb' ) as f:
        pickle.dump(obj,f)
