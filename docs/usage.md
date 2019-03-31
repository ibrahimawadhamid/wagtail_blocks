# Usage
1- Sample usage in wagtail page called "Home":
```python
from wagtail_blocks import blocks

class HomePage(Page):
    body = StreamField([
        ('header', blocks.HeaderBlock()),
        ('list', blocks.ListBlock()),
        ('image_text_overlay', blocks.ImageTextOverlayBlock()),
    ], blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel("body", classname="Full"),
    ]
```
2- For HomePage template, blocks should be rendered with IDs to function properly
```
{% for block in page.body %}
    {% include_block block with block_id=block.id %}
{% endfor %}
```