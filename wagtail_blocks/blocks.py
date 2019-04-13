import json

from django import forms

try:
    from wagtail.wagtailcore import blocks
    from wagtail.wagtailimages.blocks import ImageChooserBlock

    wagtail_version = 1

except ImportError:
    from wagtail.core import blocks
    from wagtail.images.blocks import ImageChooserBlock

    wagtail_version = 2


class HeaderChoiceBlock(blocks.ChoiceBlock):
    choices = (
        ('h1', 'H1'),
        ('h2', 'H2'),
        ('h3', 'H3'),
        ('h4', 'H4'),
        ('h5', 'H5'),
        ('h6', 'H6'),
    )


class HeaderBlock(blocks.StructBlock):
    header = HeaderChoiceBlock(
        label='Header Size',
    )
    text = blocks.CharBlock(
        label='Text',
        max_length=50,
    )

    class Meta:
        template = 'wagtail_blocks/header.html'
        icon = "title"


class ListBlock(blocks.StructBlock):
    content = blocks.ListBlock(
        blocks.CharBlock(),
        label='Items',
    )

    class Meta:
        template = 'wagtail_blocks/list.html'
        icon = "list-ul"


class ImageTextOverlayBlock(blocks.StructBlock):
    image = ImageChooserBlock(
        label='Image',
    )
    text = blocks.CharBlock(
        label='Text',
        max_length=200,
    )

    class Meta:
        template = 'wagtail_blocks/image_text_overlay.html'
        icon = 'fa-image'


class SingleImageWithText(blocks.StructBlock):
    image = ImageChooserBlock(
        label='Image',
    )
    text = blocks.CharBlock(
        label='Text',
        max_length=200,
    )


class CroppedImagesWithTextBlock(blocks.StructBlock):
    image_items = blocks.ListBlock(
        SingleImageWithText(),
        label="Image Item",
    )

    class Meta:
        template = 'wagtail_blocks/cropped_images_with_text.html'
        icon = 'fa-camera-retro'


class SingleListImage(blocks.StructBlock):
    image = ImageChooserBlock(
        label='Image',
    )
    title = blocks.CharBlock(
        label='Title',
        max_length=200,
    )
    text = blocks.CharBlock(
        label='Text',
        max_length=200,
    )
    link_text = blocks.CharBlock(
        label='Link Text',
        max_length=200,
        required=False,
    )
    link_url = blocks.URLBlock(
        label='Link URL',
        max_length=200,
        required=False,
    )


class ListWithImagesBlock(blocks.StructBlock):
    list_items = blocks.ListBlock(
        SingleListImage(),
        label="List Item",
    )

    class Meta:
        template = 'wagtail_blocks/list_with_images.html'
        icon = 'fa-id-card-o'


class SingleThumbnail(blocks.StructBlock):
    image = ImageChooserBlock(
        label='Image',
    )


class ThumbnailGalleryBlock(blocks.StructBlock):
    image_items = blocks.ListBlock(
        SingleThumbnail(),
        label="Image",
    )

    class Meta:
        template = 'wagtail_blocks/thumbnail_gallery.html'
        icon = 'fa-object-ungroup'


class ChartChoiceBlock(blocks.ChoiceBlock):
    choices = (
        ('bar', 'Bar'),
        ('horizontalBar', 'Horizontal Bar'),
        ('pie', 'Pie'),
        ('doughnut', 'Doughnut'),
        ('polarArea', 'Polar Area'),
        ('radar', 'Radar'),
        ('line', 'Line'),
    )


class ChartDataset(blocks.StructBlock):
    label = blocks.CharBlock(
        label='Dataset Label',
        max_length=120,
        default='Dataset #1',
    )
    dataset_data = blocks.ListBlock(
        blocks.IntegerBlock(),
        label='Data',
        default='0',
    )


class ChartBlock(blocks.StructBlock):
    title = blocks.CharBlock(
        label='Title',
        max_length=120,
        default='Chart Title',
    )
    chart_type = ChartChoiceBlock(
        label='Chart Type',
        default='bar'
    )
    labels = blocks.ListBlock(
        blocks.CharBlock(max_length=40, label="Label", default='Label'),
        label='Chart Labels',
    )
    datasets = blocks.ListBlock(
        ChartDataset(),
        label='Dataset',
    )

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        value['datasets'] = json.dumps(value['datasets'])
        return context

    class Meta:
        template = 'wagtail_blocks/chart.html'
        icon = 'fa-bar-chart'


class MapBlock(blocks.StructBlock):
    marker_title = blocks.CharBlock(max_length=120,
                                    default="Marker Title 'This will be updated after you save changes.'")
    marker_description = blocks.RichTextBlock()
    zoom_level = blocks.IntegerBlock(min_value=0, max_value=18, default='2', required=False)
    location_x = blocks.FloatBlock(default='35.0', required=False)
    location_y = blocks.FloatBlock(default='0.16', required=False)
    marker_x = blocks.FloatBlock(default='51.5', required=False)
    marker_y = blocks.FloatBlock(default='-0.09', required=False)

    @property
    def media(self):
        return forms.Media(
            js=["https://unpkg.com/leaflet@1.4.0/dist/leaflet.js"],
            css={'all': ["https://unpkg.com/leaflet@1.4.0/dist/leaflet.css"]}
        )

    class Meta:
        form_template = 'wagtail_blocks/admin_blocks/map.html'
        template = 'wagtail_blocks/map.html'
        icon = "fa-globe"


class SingleImageSlide(blocks.StructBlock):
    image = ImageChooserBlock(
        label='Image',
    )


class ImageSliderBlock(blocks.StructBlock):
    image_items = blocks.ListBlock(
        SingleImageSlide(),
        label="Image",
    )

    class Meta:
        template = 'wagtail_blocks/image_slider.html'
        icon = 'fa-slideshare'
