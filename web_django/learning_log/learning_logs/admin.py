from django.contrib import admin
from .models import Entry, Topic  # .modes -> 当前目录的models


# Register your models here.
admin.site.register(Topic)  # 让Django通过管理网站管理Topic模型
admin.site.register(Entry)  # 让Django通过管理网站管理Entry模型
