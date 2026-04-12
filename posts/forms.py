from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'slug', 'image']   # 把你想要的字段都写上
        
        # 可选：给图片字段加中文标签
        labels = {
            'title': '标题',
            'body': '正文',
            'slug': '友好网址 (slug)',
            'image': '封面图片',
        }