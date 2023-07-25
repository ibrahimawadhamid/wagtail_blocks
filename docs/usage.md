# Usage

In your page model, inside the streamfield you can add any type of the available blocks.

Sample usage in wagtail page called "Home":

```python
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel

from wagtail_blocks.blocks import (
    HeaderBlock,
    ListBlock,
    ImageTextOverlayBlock,
    CroppedImagesWithTextBlock,
    ListWithImagesBlock,
    ThumbnailGalleryBlock,
    ChartBlock,
    MapBlock,
    ImageSliderBlock,
)

class HomePage(Page):
    body = StreamField([
        ('header', HeaderBlock()),
        ('list', ListBlock()),
        ('image_text_overlay', ImageTextOverlayBlock()),
        ('cropped_images_with_text', CroppedImagesWithTextBlock()),
        ('list_with_images', ListWithImagesBlock()),
        ('thumbnail_gallery', ThumbnailGalleryBlock()),
        ('chart', ChartBlock()),
        ('map', MapBlock()),
        ('image_slider', ImageSliderBlock()),
    ], blank=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]
```

For HomePage template, blocks should be rendered with IDs to function properly

```html
{% for block in page.body %}
    {% include_block block with block_id=block.id %}
{% endfor %}
```
