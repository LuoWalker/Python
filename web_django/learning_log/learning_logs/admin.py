from django.contrib import admin
from .models import Topic  # .modes -> 当前目录的models


# Register your models here.
admin.site.register(Topic)  # 让Django通过管理网站管理Topic模型
