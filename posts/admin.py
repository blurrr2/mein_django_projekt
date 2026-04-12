from django.contrib import admin
from .models import Post, PostImage

class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 3   # 默认显示 3 个上传框

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageInline]
    list_display = ['title', 'category', 'date']
    list_filter = ['category']

admin.site.register(PostImage)