# Author:JZW
import os
import sys
import django

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mini_app.settings")
django.setup()

from api import models

models.UserInfo.objects.create(
    phone='15840665440',
    nickname='姜姜-0',
    avatar='https://mini-1304610462.cos.ap-beijing.myqcloud.com/rbejfspx1610762220508.jpg'
)
models.UserInfo.objects.create(
    phone='15840665411',
    nickname='姜姜-1',
    avatar='https://mini-1304610462.cos.ap-beijing.myqcloud.com/rbejfspx1610762220508.jpg'
)
models.UserInfo.objects.create(
    phone='15840665332',
    nickname='姜姜-2',
    avatar='https://mini-1304610462.cos.ap-beijing.myqcloud.com/rbejfspx1610762220508.jpg'
)
models.UserInfo.objects.create(
    phone='15840665333',
    nickname='姜姜-3',
    avatar='https://mini-1304610462.cos.ap-beijing.myqcloud.com/rbejfspx1610762220508.jpg'
)
models.UserInfo.objects.create(
    phone='15840665334',
    nickname='姜姜-4',
    avatar='https://mini-1304610462.cos.ap-beijing.myqcloud.com/rbejfspx1610762220508.jpg'
)