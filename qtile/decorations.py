from qtile_extras.widget.decorations import RectDecoration

from colors import ayu_dark as color


# Base widget decoration without color
decor_base = {
    'decorations': [
        RectDecoration(
            colour=color['ui']['bg'],
            radius=0,
            filled=True,
            padding_y=0
        )
    ],
    'padding': 16
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
            colour=color['editor']['fg'],
            radius=4,
            filled=True,
            padding_y=2
        )
    ],
    'padding': 16
}