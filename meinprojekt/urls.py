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
    # Django 传统 admin（可选，改名避免冲突）
    path('django-admin/', admin.site.urls),

    # Wagtail 管理后台（最重要的）
    path('admin/', include(wagtailadmin_urls)),

    # Wagtail 文档
    path('documents/', include(wagtaildocs_urls)),

    # 你的文章分类路由（必须放在 Wagtail catch-all 之前）
    path('', include('posts.urls', namespace='posts')),

    # 首页
    path('', homepage, name='home'),

    # Wagtail 页面路由（必须放在最后！）
    path('', include(wagtail_urls)),
]

# 开发环境下允许访问媒体文件
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)