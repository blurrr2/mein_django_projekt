from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.images.blocks import ImageChooserBlock   # 可选

class Post(Page):
    """Wagtail 博客文章模型"""

    date = models.DateField("date", auto_now_add=False)
    category = models.CharField(
        max_length=50,
        choices=[
            ('germany', 'Deutschland verstehen'),
            ('german-learning', 'Deutsch lernen'),
            ('coding', 'Coding Journey'),
        ],
        default='german-learning',
    )
    featured_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    body = RichTextField("body", blank=True)

    # Wagtail 后台编辑面板
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('category'),
            FieldPanel('featured_image'),
        ], heading="article information"),
        FieldPanel('body'),
    ]

    template = "posts/post_detail.html"   # 使用你已有的模板

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"