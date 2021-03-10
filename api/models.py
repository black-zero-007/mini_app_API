from django.db import models

# Create your models here.
class UserInfo(models.Model):
    phone = models.CharField(verbose_name='手机号',max_length=11,unique=True)
    nickname = models.CharField(verbose_name='昵称',max_length=64)
    avatar = models.CharField(verbose_name='头像',max_length=256,null=True)
    token = models.CharField(verbose_name='用户Token',max_length=64,blank=True)

    fans_count = models.PositiveIntegerField(verbose_name='粉丝数',default=0)
    follow = models.ManyToManyField(verbose_name='关注',to='self',blank=True,symmetrical=False)

    balance = models.PositiveIntegerField(verbose_name='账户余额',default=0)
    session_key = models.CharField(verbose_name='微信会话密钥',max_length=32)
    openid = models.CharField(verbose_name='微信用户唯一标识',max_length=32)

    def __str__(self):
        return self.nickname

class Topic(models.Model):
    """
    话题
    """
    title = models.CharField(verbose_name='话题',max_length=32)
    count = models.PositiveIntegerField(verbose_name='关注度',default=0)

class News(models.Model):
    """
    动态
    """
    cover = models.CharField(verbose_name='封面',max_length=128)
    content = models.CharField(verbose_name='内容',max_length=255)
    topic = models.ForeignKey(verbose_name='话题',to='Topic',null=True,blank=True,on_delete=models.CASCADE)
    address = models.CharField(verbose_name='位置',max_length=128,null=True,blank=True)

    user = models.ForeignKey(verbose_name='发布者',to='UserInfo',related_name='news',on_delete=models.CASCADE)

    favor_count = models.PositiveIntegerField(verbose_name='点赞数',default=0)
    viewer_count = models.PositiveIntegerField(verbose_name='浏览数',default=0)
    comment_count = models.PositiveIntegerField(verbose_name='评论数',default=0)
    collect_count = models.PositiveIntegerField(verbose_name='收藏数',default=0)
    create_time = models.DateTimeField(verbose_name='发布时间',auto_now_add=True)

class NewsDetail(models.Model):
    key = models.CharField(verbose_name='腾讯对象存储中文件名',max_length=128,help_text='用于以后在腾讯对象存储中删除')
    cos_path = models.CharField(verbose_name='腾讯对象存储中图片路径',max_length=128)
    news = models.ForeignKey(verbose_name='动态',to='News',on_delete=models.CASCADE)

class ViewerRecord(models.Model):
    """
    浏览记录
    """
    user = models.ForeignKey(verbose_name='用户',to='UserInfo',on_delete=models.CASCADE)
    news = models.ForeignKey(verbose_name='动态',to='News',on_delete=models.CASCADE)
    
class TopicViewerRecord(models.Model):
    user = models.ForeignKey(verbose_name='用户',to=UserInfo,on_delete=models.CASCADE)
    topic = models.ForeignKey(verbose_name='话题',to=Topic,on_delete=models.CASCADE)

class NewsFavorRecord(models.Model):
    """
    动态点赞记录表
    """
    user = models.ForeignKey(verbose_name='点赞用户', to='UserInfo', on_delete=models.CASCADE)
    news = models.ForeignKey(verbose_name='动态', to='News', on_delete=models.CASCADE)

class CommentRecord(models.Model):
    """
    评论表
    """
    comment = models.CharField(verbose_name='评论内容',max_length=255)
    user = models.ForeignKey(verbose_name='评论者',to='UserInfo',on_delete=models.CASCADE)
    news = models.ForeignKey(verbose_name='动态',to='News',on_delete=models.CASCADE)
    create_date = models.DateTimeField(verbose_name='评论时间',auto_now_add=True)

    reply = models.ForeignKey(verbose_name='回复对象',to='self',null=True,blank=True,related_name='replys',on_delete=models.CASCADE)
    depth = models.PositiveIntegerField(verbose_name='层级数',default=1)
    root = models.ForeignKey(verbose_name='根评论',to='self',blank=True,null=True,related_name='roots',on_delete=models.CASCADE)
    favor_count = models.PositiveIntegerField(verbose_name='点赞数',default=0)

class CommentFavorRecord(models.Model):
    """
    评论赞
    """
    comment = models.ForeignKey(verbose_name='评论',to='CommentRecord',on_delete=models.CASCADE)
    user = models.ForeignKey(verbose_name='用户',to='UserInfo',on_delete=models.CASCADE)

class NewsCollectRecord(models.Model):
    """
    文章收藏表
    """
    user = models.ForeignKey(verbose_name='用户',to=UserInfo,on_delete=models.CASCADE)
    news = models.ForeignKey(verbose_name='文章',to=News,on_delete=models.CASCADE)




