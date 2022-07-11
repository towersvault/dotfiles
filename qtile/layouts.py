"""
Group layouts
"""


from libqtile import layout

import colors2


layouts = [
    layout.Columns(
        border_focus=colors2.BLUE,
        border_focus_stack=colors2.BLUE,
        border_normal=colors2.SURFACE_0,
        border_normal_stack=colors2.SURFACE_0,
        margin=8,
        border_width=1
    ),
    layout.Max()
]