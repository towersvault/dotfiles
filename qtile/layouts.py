"""
Group layouts
"""


from libqtile import layout

import colors


layouts = [
    layout.Columns(
        border_focus=colors.NORMAL_BLUE,
        border_focus_stack=colors.NORMAL_BLUE,
        border_normal=colors.NORMAL_BLACK,
        border_normal_stack=colors.NORMAL_BLACK,
        margin=8,
        border_width=1
    ),
    layout.Max()
]