from django.shortcuts import render
from .models import Post

# ==================== Category List Views ====================
def germany_list(request):
    posts = Post.objects.live().filter(category='germany').order_by('-publish_date')
    return render(request, 'posts/posts_list.html', {
        'posts': posts,
        'title': 'Deutschland verstehen',
        'category': 'germany'
    })

def german_learning_list(request):
    posts = Post.objects.live().filter(category='german-learning').order_by('-publish_date')
    return render(request, 'posts/posts_list.html', {
        'posts': posts,
        'title': 'Deutsch lernen',
        'category': 'german-learning'
    })

def coding_list(request):
    posts = Post.objects.live().filter(category='coding').order_by('-publish_date')
    return render(request, 'posts/posts_list.html', {
        'posts': posts,
        'title': 'Coding Journey',
        'category': 'coding'
    })