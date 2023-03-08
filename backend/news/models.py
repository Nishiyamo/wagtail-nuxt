from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtail_headless_preview.models import HeadlessMixin


class NewsPage(HeadlessMixin, Page):
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body'),
    ]

    api_fields = [
        APIField('intro'),
        APIField('body'),
    ]
