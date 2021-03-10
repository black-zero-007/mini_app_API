# Author:JZW
import os
import sys
import django



base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mini_app.settings")
django.setup()
from api import models
for i in range(1,50):
    if i%2 != 0:
        new_object = models.News.objects.create(
            cover='https://mini-1304610462.cos.ap-beijing.myqcloud.com/6pvi3mao1610795130475.jpg',
            content='想念小宝的第{0}天'.format(i),
            topic_id='1',
            user_id='1'
        )
        models.NewsDetail.objects.create(
            key='6pvi3mao1610795130475.jpg',
            cos_path='https://mini-1304610462.cos.ap-beijing.myqcloud.com/6pvi3mao1610795130475.jpg',
            news=new_object
        )
        models.NewsDetail.objects.create(
            key='0w0s1nx71610762098614.jpg',
            cos_path='https://mini-1304610462.cos.ap-beijing.myqcloud.com/0w0s1nx71610762098614.jpg',
            news=new_object
        )
    else:
        new_object = models.News.objects.create(
            cover='https://mini-1304610462.cos.ap-beijing.myqcloud.com/7xvd78tc1610762486866.jpg',
            content='想念小宝的第{0}天'.format(i),
            topic_id='1',
            user_id='1'
        )
        models.NewsDetail.objects.create(
            key='7xvd78tc1610762486866.jpg',
            cos_path='https://mini-1304610462.cos.ap-beijing.myqcloud.com/7xvd78tc1610762486866.jpg',
            news=new_object
        )
        models.NewsDetail.objects.create(
            key='0w0s1nx71610762098614.jpg',
            cos_path='https://mini-1304610462.cos.ap-beijing.myqcloud.com/0w0s1nx71610762098614.jpg',
            news=new_object
        )