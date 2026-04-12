from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from meinprojekt.views import homepage, about

urlpatterns = [
    path('admin/', admin.site.urls),

    # 首页
    path('', homepage, name='home'),
    
    # 德国了解（直接用 posts app 处理）
    path('germany/', include('posts.urls')),
    
    # 德语学习
    path('german-learning/', include('posts.urls')),
    
    # 编程学习
    path('coding/', include('posts.urls')),

    # 如果以后想保留原来的 /posts/ 列表页，也可以保留
    # path('posts/', include('posts.urls')),
]

# 开发环境下允许访问上传的图片
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)