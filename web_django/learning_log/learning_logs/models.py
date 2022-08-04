from cgitb import text
from django.db import models

# Create your models here.


class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)  # 储存用户写的主题
    date_added = models.DateTimeField(auto_now_add=True)  # 自动标记文件创建时的时间

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text


class Entry(models.Model):
    """学到有关某个主题的相关知识"""
    # 让每条数据关联到特定的Topic，CASCADE指删除Topic时条目一起删除
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """用于储存额外数据"""
        # 使用entries展示多个条目，默认为entrys
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回模型的字符串表示"""
        # 只展示前50个字符
        if(len(self.text)>50):
            return f"{self.text[:50]}..."
        else:
            return self.text[:50]
