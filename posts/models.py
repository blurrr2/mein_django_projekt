from django.db import models
from django.utils.timezone import localdate

from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

from wagtail.blocks import (
    RichTextBlock,
    RawHTMLBlock,
)

from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtailmarkdown.blocks import MarkdownBlock
from wagtail.embeds.blocks import EmbedBlock


class Post(Page):
    """Wagtail 博客文章模型（支持多种格式）"""

    publish_date = models.DateField(
        verbose_name="publish date",
        default=localdate,
    )

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

    body = StreamField([
        ('rich_text', RichTextBlock(label="Rich text", icon="doc-full")),
        ('markdown', MarkdownBlock(label="Markdown", icon="code")),
        ('image', ImageChooserBlock(label="Image", icon="image")),
        ('embed', EmbedBlock(label="Embed media", icon="media")),
        ('table', TableBlock(label="Table", icon="table")),
        ('raw_html', RawHTMLBlock(label="Raw HTML", icon="code")),
    ], use_json_field=True, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('publish_date'),
            FieldPanel('category'),
            FieldPanel('featured_image'),
        ], heading="Article Information"),
        FieldPanel('body'),
    ]

    template = "posts/post_detail.html"

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"