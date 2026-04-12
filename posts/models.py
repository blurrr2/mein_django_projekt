from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    
    category = models.CharField(
        max_length=50,
        choices=[
            ('germany', 'deutschland verstehen'),
            ('german-learning', 'deutsch lernen'),
            ('coding', 'coding journey'),
        ],
        default='coding'
    )

    def __str__(self):
        return self.title


# ==================== 新增：支持一篇文章多张图片 ====================
class PostImage(models.Model):
    post = models.ForeignKey(
        Post, 
        on_delete=models.CASCADE, 
        related_name='images'
    )
    image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.post.title}"