"""定义learning_logs的url模式"""
from django import apps
from django.urls import URLPattern, path
from . import views

apps.name = 'learning_logs'

"""
为每个试图定义url：path('url', 'view', '别名')
识别到匹配的url，调用相应的view
"""
urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    path('topics', views.topics, name='topics')

]
