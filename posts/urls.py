from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('germany/', views.germany_list, name='germany_list'),
    path('german-learning/', views.german_learning_list, name='german_learning_list'),
    path('coding/', views.coding_list, name='coding_list'),
]