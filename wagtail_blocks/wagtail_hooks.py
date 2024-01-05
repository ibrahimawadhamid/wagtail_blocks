from wagtail import hooks

@hooks.register("register_icons")
def register_icons(icons):
    return icons + [
        "wagtailfontawesomesvg/solid/camera-retro.svg",
        "wagtailfontawesomesvg/solid/id-card-clip.svg",
        "wagtailfontawesomesvg/solid/object-ungroup.svg",
        "wagtailfontawesomesvg/solid/chart-column.svg",
        "wagtailfontawesomesvg/solid/sliders.svg",
    ]
