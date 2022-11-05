from qtile_extras.widget.decorations import RectDecoration

from colors import ayu_dark as color


# Base widget decoration without color
decor_base = {
    'decorations': [
        RectDecoration(
            colour=color['ui']['bg'],
            # radius=18,
            # filled=True,
            padding_y=6,
            # group=True,
            clip=True
        )
    ],
    'padding': 6
}


decor_groupbox = {
    'decorations': [
        RectDecoration(
            colour=color['editor']['indentGuide']['normal'],
            radius=18,
            filled=True,
            padding_y=6,
            group=True
        )
    ],
    'padding': 16
}


# Power decoration
decor_power = {
    'decorations': [],
    'padding': 12
}

# Clock emoji decoration
decor_widget_title = {
    'decorations': [
        RectDecoration(
            colour=color['editor']['line'],
            radius=0,
            filled=True,
            padding_y=0
        )
    ],
    'padding': 16
}

# Prompt decoration
decor_prompt = {
    'decorations': [
        RectDecoration(
            colour=color['editor']['indentGuide']['normal'],
            radius=18,
            filled=True,
            padding_y=6,
            group=True
        )
    ],
    'padding': 16
}