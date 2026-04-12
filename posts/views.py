from django.shortcuts import render, redirect
from django.http import Http404
from .models import Post
from .forms import PostForm

# ==================== 原有函数 ====================
def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', {'posts': posts})

def post_detail(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        raise Http404("这篇文章不存在")
    return render(request, 'posts/post_detail.html', {'post': post})

# ==================== 新增的三个板块视图 ====================
def germany_list(request):
    """德国了解 列表页"""
    posts = Post.objects.filter(category='germany').order_by('-date')
    return render(request, 'posts/posts_list.html', {
        'posts': posts,
        'title': 'Deutschland verstehen'
    })

def german_learning_list(request):
    """德语学习 列表页"""
    posts = Post.objects.filter(category='german-learning').order_by('-date')
    return render(request, 'posts/posts_list.html', {
        'posts': posts,
        'title': 'Deutsch lernen'
    })

def coding_list(request):
    """编程学习 列表页"""
    posts = Post.objects.filter(category='coding').order_by('-date')
    return render(request, 'posts/posts_list.html', {
        'posts': posts,
        'title': 'Coding Journey'
    })

# 创建文章（上传图片用）
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:posts_list')
    else:
        form = PostForm()
    return render(request, 'posts/post_create.html', {'form': form})