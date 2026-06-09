from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from meinprojekt.views import homepage, about

# Wagtail
from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

urlpatterns = [
    # Django 传统 admin
    path('django-admin/', admin.site.urls),

    # Wagtail 管理后台
    path('admin/', include(wagtailadmin_urls)),

    # Wagtail 文档
    path('documents/', include(wagtaildocs_urls)),

    # 首页（必须用具体路径，不能和 posts.urls / wagtail_urls 同用空前缀）
    path('', homepage, name='home'),

    # 文章分类列表路由
    path('posts/', include('posts.urls', namespace='posts')),

    # Wagtail 页面路由（必须放在最后，负责所有 Page 详情）
    path('', include(wagtail_urls)),
]

# 开发环境下允许访问媒体文件
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)