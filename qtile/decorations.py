from qtile_extras.widget.decorations import RectDecoration

import colors2


# Base widget decoration without color
decor_base = {
    'decorations': [
        RectDecoration(
            colour=colors2.MANTLE,
            radius=4,
            filled=True,
            padding_y=2
        )
    ],
    'padding': 16
}

# Clock emoji decoration
decor_clock = {
    'decorations': [
        RectDecoration(
            colour=colors2.RED,
            radius=4,
            filled=True,
            padding_y=2
        )
    ],
    'padding': 16
}

# WiFi emoji decoration
decor_wifi = {
    'decorations': [
        RectDecoration(
            colour=colors2.MAUVE,
            radius=4,
            filled=True,
            padding_y=2
        )
    ],
    'padding': 16
}

# Sound emoji decoration
decor_sound = {
    'decorations': [
        RectDecoration(
            colour=colors2.BLUE,
            radius=4,
            filled=True,
            padding_y=2
        )
    ],
    'padding': 16
}

# Display brightness emoji decoration
decor_brightness = {
    'decorations': [
        RectDecoration(
            colour=colors2.YELLOW,
            radius=4,
            filled=True,
            padding_y=2
        )
    ],
    'padding': 16
}

# Battery emoji decoration
decor_battery = {
    'decorations': [
        RectDecoration(
            colour=colors2.GREEN,
            radius=4,
            filled=True,
            padding_y=2
        )
    ],
    'padding': 16
}

# Prompt decoration
decor_prompt = {
    'decorations': [
        RectDecoration(
            colour=colors2.TEXT,
            radius=4,
            filled=True,
            padding_y=2
        )
    ],
    'padding': 16
}