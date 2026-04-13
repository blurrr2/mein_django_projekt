from django.shortcuts import render
from django.http import Http404
from .models import Post

# ==================== Category List Views ====================
def germany_list(request):
    posts = Post.objects.live().filter(category='germany').order_by('-date')
    return render(request, 'posts/posts_list.html', {
        'posts': posts,
        'title': 'Deutschland verstehen',
        'category': 'germany'
    })

def german_learning_list(request):
    posts = Post.objects.live().filter(category='german-learning').order_by('-date')
    return render(request, 'posts/posts_list.html', {
        'posts': posts,
        'title': 'Deutsch lernen',
        'category': 'german-learning'
    })

def coding_list(request):
    posts = Post.objects.live().filter(category='coding').order_by('-date')
    return render(request, 'posts/posts_list.html', {
        'posts': posts,
        'title': 'Coding Journey',
        'category': 'coding'
    })

def post_detail(request, slug):
    try:
        post = Post.objects.live().get(slug=slug)
    except Post.DoesNotExist:
        raise Http404("This post does not exist")
    return render(request, 'posts/post_detail.html', {'post': post})