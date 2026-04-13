from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.blocks import RichTextBlock, RawHTMLBlock
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.images.blocks import ImageChooserBlock

class Post(Page):
    """Wagtail 博客文章模型（支持 Raw HTML 块）"""

    date = models.DateField("date published")
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
    
    # ← 这里改成 StreamField，支持 Raw HTML 块
    body = StreamField([
        ('rich_text', RichTextBlock()),
        ('raw_html', RawHTMLBlock()),      # ← 新增 Raw HTML 块
    ], use_json_field=True, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('category'),
            FieldPanel('featured_image'),
        ], heading="article information"),
        FieldPanel('body'),
    ]

    template = "posts/post_detail.html"

    class Meta:
        verbose_name = "blog post"
        verbose_name_plural = "blog posts"