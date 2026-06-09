from django.db import models
from django.utils import timezone

from wagtail.models import Page
from wagtail.fields import StreamField
# 1. 导入必要的 Panel
from wagtail.admin.panels import FieldPanel, MultiFieldPanel 

from wagtail.blocks import (
    RichTextBlock, 
    RawHTMLBlock,  
    BlockQuoteBlock,  # 2. 修正引用块的名称
)

# 3. 单独导入 TableBlock
from wagtail.contrib.table_block.blocks import TableBlock

from wagtail.images.blocks import ImageChooserBlock
from wagtailmarkdown.blocks import MarkdownBlock

from wagtail.embeds.blocks import EmbedBlock

#from wagtailcodeblock.blocks import CodeBlock



class Post(Page):
    """Wagtail 博客文章模型（支持 Raw HTML 块）"""

    date = models.DateField(
        verbose_name="发布日期",
        default=timezone.now,
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
        # 如果没有安装代码块插件，建议先用 StructBlock 自己写一个，或者暂时注释掉：
        #('code', CodeBlock(label="code", icon="code")),
        ('image', ImageChooserBlock(label="image", icon="image")),
        ('embed', EmbedBlock(label="media", icon="media")),
        ('table', TableBlock(label="table", icon="table")),
        ('quote', BlockQuoteBlock(label="quote", icon="openquote")), # 已修正为 BlockQuoteBlock
        ('raw_html', RawHTMLBlock(label="Raw HTML", icon="code")),
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