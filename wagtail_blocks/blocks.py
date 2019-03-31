from wagtail.core.blocks import ChoiceBlock, StructBlock, CharBlock


class HeaderChoiceBlock(ChoiceBlock):
    choices = (
        ('h1', 'H1'),
        ('h2', 'H2'),
        ('h3', 'H3'),
        ('h4', 'H4'),
        ('h5', 'H5'),
        ('h6', 'H6'),
    )


class HeaderBlock(StructBlock):
    header = HeaderChoiceBlock(
        label='Header Size',
    )
    text = CharBlock(
        label='Text',
        max_length=50,
    )

    class Meta:
        template = 'wagtail_blocks/header.html'
        icon = "title"
