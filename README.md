# wagtail_blocks ![wagtail](https://img.shields.io/badge/CMS-Wagtail-green.svg)
[![PyPI](https://img.shields.io/pypi/v/wagtail-blocks.svg)](https://pypi.python.org/pypi/wagtail-blocks) ![PyPI - License](https://img.shields.io/pypi/l/wagtail-blocks.svg) ![Build](https://img.shields.io/pypi/status/wagtail-blocks.svg)

A Collection of awesome Wagtail CMS stream-field blocks.

## Quickstart

You must have your [Wagtail](https://wagtail.io/) project up and running:

```sh
pip install wagtail_blocks
```
Add wagtail-blocks to your `settings.py` in the INSTALLED_APPS section, before the core wagtail packages:

```python
'wagtail_blocks',
```

## Sample Usage
```python
from wagtail_blocks import blocks

class HomePage(Page):
    body = StreamField([
        ('header', blocks.HeaderBlock()),
    ], blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel("body", classname="Full"),
    ]
```

## Available Blocks
Check [Screenshots](https://github.com/ibrahimawadhamid/wagtail_blocks/tree/master/screenshots)
- Header Block

## Supported Versions
![wagtail](https://img.shields.io/badge/Wagtail-2.x-green.svg) ![Python](https://img.shields.io/pypi/pyversions/wagtail-blocks.svg)
