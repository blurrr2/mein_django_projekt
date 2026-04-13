from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # 分类列表
    path('germany/', views.germany_list, name='germany_list'),
    path('german-learning/', views.german_learning_list, name='german_learning_list'),
    path('coding/', views.coding_list, name='coding_list'),

    # 文章详情 — 加上 germany/ 前缀匹配实际 URL
    path('germany/<slug:slug>/', views.post_detail, name='post_detail'),
    path('german-learning/<slug:slug>/', views.post_detail, name='post_detail_german'),
    path('coding/<slug:slug>/', views.post_detail, name='post_detail_coding'),
]