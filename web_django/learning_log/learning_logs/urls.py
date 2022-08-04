"""定义learning_logs的url模式"""
from django.urls import URLPattern, path, include
from . import views

app_name = 'learning_logs'

"""
为每个试图定义url：path('url', 'view', '别名')
识别到匹配的url，调用相应的view
"""
urlpatterns = [
    path('', views.index, name='index'),  # 主页
    path('topics/', views.topics, name='topics'),  # 主题列表
    path('topic/<int:topic_id>/', views.topic, name='topic'),  # 特定主题
    path('new_topic/', views.new_topic, name='new_topic'),  # 新建主题
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),  # 新建条目
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),  # 修改条目

]
