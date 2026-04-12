from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # 德国了解
    path('', views.germany_list, name='germany_list'),
    
    # 德语学习
    path('german-learning/', views.german_learning_list, name='german_learning_list'),
    
    # 编程学习
    path('coding/', views.coding_list, name='coding_list'),
    
    # 文章详情页（所有板块共用）
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]