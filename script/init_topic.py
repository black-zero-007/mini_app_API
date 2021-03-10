# Author:JZW
import os
import sys
import django



base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mini_app.settings")
django.setup()

from api import models
models.Topic.objects.create(title="2021哔哩哔哩万岁")
models.Topic.objects.create(title="辽工大放假啦")
models.Topic.objects.create(title="河南新增感染人数59人")
models.Topic.objects.create(title="今天你吃饺子了嘛")
models.Topic.objects.create(title="漫展麻衣学姐事件")