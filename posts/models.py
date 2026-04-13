from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.blocks import RichTextBlock, RawHTMLBlock
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.images.models import Image


class Post(Page):
    """Wagtail Post Page"""

    template = "posts/post_detail.html"

    publish_date = models.DateField("Publish Date")

    category = models.CharField(
        max_length=50,
        choices=[
            ('germany', 'deutschland verstehen'),
            ('german-learning', 'deutsch lernen'),
            ('coding', 'coding journey'),
        ],
        default='coding',
        verbose_name="Category"
    )

    featured_image = models.ForeignKey(
        Image,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Featured Image"
    )

    body = StreamField([
        ('rich_text', RichTextBlock(
            features=['h2', 'h3', 'h4', 'bold', 'italic', 'link', 'code', 'image', 'hr', 'blockquote'],
            label="Rich Text"
        )),
        ('raw_html', RawHTMLBlock(label="Raw HTML")),
    ], blank=True, use_json_field=True, verbose_name="Body")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('publish_date'),
            FieldPanel('category'),
            FieldPanel('featured_image'),
        ], heading="Post Information"),
        FieldPanel('body'),
    ]

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

    def __str__(self):
        return self.title