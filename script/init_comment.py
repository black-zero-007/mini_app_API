# Author:JZW
import os
import sys
import django



base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mini_app.settings")
django.setup()

from api import models
# first1 = models.CommentRecord.objects.create(
#     news_id=5,
#     comment='1',
#     user_id=1,
#     depth=1
# )
# first1_1 = models.CommentRecord.objects.create(
#     news_id=5,
#     comment='1_1',
#     user_id=3,
#     reply=first1,
#     depth=2,
#
# )
# first1_1_1 = models.CommentRecord.objects.create(
#     news_id=5,
#     comment='1_1_1',
#     user_id=4,
#     reply=first1_1,
#     depth=3
# )
first2 = models.CommentRecord.objects.create(
    news_id=4,
    comment='2',
    user_id=2,
    depth=1
)