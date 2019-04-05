# wagtail_blocks ![wagtail](https://img.shields.io/badge/CMS-Wagtail-green.svg)
[![PyPI](https://img.shields.io/pypi/v/wagtail-blocks.svg)](https://pypi.python.org/pypi/wagtail-blocks) ![Build](https://travis-ci.org/ibrahimawadhamid/wagtail_blocks.svg?branch=master) ![Build](https://img.shields.io/pypi/status/wagtail-blocks.svg) [![Documentation Status](https://readthedocs.org/projects/wagtail-blocks/badge/?version=latest)](https://wagtail-blocks.readthedocs.io/en/latest/?badge=latest) ![PyPI - License](https://img.shields.io/pypi/l/wagtail-blocks.svg)

A Collection of awesome Wagtail CMS stream-field blocks and Charts.
*Check out [Awesome Wagtail](https://github.com/springload/awesome-wagtail) for more awesome packages and resources from the Wagtail community.*

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
    ListWithImagesBlock, ThumbnailGalleryBlock, ChartBlock

class HomePage(Page):
    body = StreamField([
        ('header', HeaderBlock()),
        ('list', ListBlock()),
        ('image_text_overlay', ImageTextOverlayBlock()),
        ('cropped_images_with_text', CroppedImagesWithTextBlock()),
        ('list_with_images', ListWithImagesBlock()),
        ('thumbnail_gallery', ThumbnailGalleryBlock()),
        ('chart', ChartBlock()),
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
Check Showcase for [Standard Blocks](https://wagtail-blocks.readthedocs.io/en/latest/showcase/standard-blocks/) or [Charts](https://wagtail-blocks.readthedocs.io/en/latest/showcase/charts/) 
> - Header (H1, H2, H3, H4, H5, H6)
> - List (Unordered List)
> - Image with Text Overlay
> - Cropped Images with Text
> - List with Images and Links
> - Thumbnail Gallery
> - Chart (Bar - Pie - Line - Area - Radar)

## Supported Versions
> - Python 2 & 3
> - All wagtail versions! (1.x | 2.x)
> - Bootstrap 4

![wagtail](https://img.shields.io/badge/Wagtail-1.x|2.x-green.svg) ![Python](https://img.shields.io/pypi/pyversions/wagtail-blocks.svg) ![Boostrap](https://img.shields.io/badge/Bootstrap-4.3-blue.svg)
