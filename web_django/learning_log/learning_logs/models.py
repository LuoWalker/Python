from django.db import models

# Create your models here.


class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200) # 储存用户写的主题
    date_added = models.DateTimeField(auto_now_add=True) # 自动标记文件创建时的时间

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text
