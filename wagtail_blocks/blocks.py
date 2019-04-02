from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


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
        icon = 'fa-camera-retro'
