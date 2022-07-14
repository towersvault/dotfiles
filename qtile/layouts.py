"""
Group layouts
"""


from libqtile import layout

from colors import ayu_dark as color


layouts = [
    layout.Columns(
        border_focus=color['editor']['fg'],
        border_focus_stack=color['editor']['fg'],
        border_normal=color['editor']['bg'],
        border_normal_stack=color['editor']['bg'],
        margin=8,
        border_width=1
    ),
    layout.Max()
]