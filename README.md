# wagtail_blocks ![wagtail](https://img.shields.io/badge/CMS-Wagtail-green.svg)
[![PyPI](https://img.shields.io/pypi/v/wagtail-blocks.svg)](https://pypi.python.org/pypi/wagtail-blocks) ![Build](https://img.shields.io/pypi/status/wagtail-blocks.svg) [![Documentation Status](https://readthedocs.org/projects/wagtail-blocks/badge/?version=latest)](https://wagtail-blocks.readthedocs.io/en/latest/?badge=latest) ![PyPI - License](https://img.shields.io/pypi/l/wagtail-blocks.svg)

A Collection of awesome Wagtail CMS stream-field blocks and Charts.

*Check out [Awesome Wagtail](https://github.com/springload/awesome-wagtail) for more awesome packages and resources from the Wagtail community.*

## Note
**This project is still early on in its development lifecycle. It is possible for breaking changes to occur between versions until reaching a stable 1.0**, however we will clearly note any breaking changes between releases if applicable. Feedback and pull requests are welcome.

## Quickstart

You must have your [Wagtail](https://wagtail.io/) project up and running:

```sh
pip install wagtail_blocks
```
Add the following enteries to your `settings.py` in the INSTALLED_APPS section:

```python
'wagtailfontawesome',
'wagtail_blocks',
```

## Sample Usage
```python
from wagtail_blocks.blocks import HeaderBlock, ListBlock, ImageTextOverlayBlock, CroppedImagesWithTextBlock, \
    ListWithImagesBlock, ThumbnailGalleryBlock, ChartBlock, MapBlock, ImageSliderBlock

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
    ], blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel("body", classname="Full"),
    ]

```
### For HomePage template, blocks should be rendered with IDs to function properly
```
{% for block in page.body %}
    {% include_block block with block_id=block.id %}
{% endfor %}
```

## Available Blocks
Check Showcase for [Standard Blocks](https://wagtail-blocks.readthedocs.io/en/latest/showcase/standard-blocks/) 
or [Charts](https://wagtail-blocks.readthedocs.io/en/latest/showcase/chart/)
or [Maps](https://wagtail-blocks.readthedocs.io/en/latest/showcase/map/)
![streamfield](https://wagtail-blocks.readthedocs.io/en/latest/showcase/screenshots/streamfield.PNG)
 
> - Header (H1, H2, H3, H4, H5, H6)
> - List (Unordered List)
> - Image with Text Overlay
> - Cropped Images with Text
> - List with Images and Links
> - Thumbnail Gallery
> - Image Slider
> - Chart (Bar - Pie - Line - Area - Radar)
> - Map (Marker with rich text description)

## Supported Versions
> - Python 3.6 and higher
> - Wagtail 2 and higher
> - Bootstrap 4

