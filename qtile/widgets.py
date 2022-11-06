from libqtile import bar, layout
from libqtile.lazy import lazy
from libqtile.widget import backlight

from qtile_extras import widget
from colors import ayu_dark as color
from os import path
import decorations


widgets = [
    widget.Spacer(
        length=16
    ),

    widget.TextBox(
        '\uF848',
        fontsize=20,
        **decorations.decor_prompt
    ),

    # Prompt segment
    widget.Prompt(
        prompt='',
        cursor_color=color['editor']['fg'],
        **decorations.decor_prompt
    ),

    widget.Spacer(
        length=16
    ),

    # Window name segment
    widget.WindowName(
        format='{name}',
        **decorations.decor_base
    ),

    widget.Spacer(
        length=bar.STRETCH
    ),

    widget.TextBox(
        '\uF574',
        foreground=color['syntax']['keyword'],
        fontsize=20,
        mouse_callbacks={'Button1': lazy.spawn('systemctl hibernate')},
        **decorations.decor_groupbox
    ),

    widget.TextBox(
        '\uF6D8',
        foreground=color['editor']['indentGuide']['active'],
        fontsize=20,
        **decorations.decor_groupbox
    ),

    # Group box segment
    widget.GroupBox(
        highlight_method="font",
        active=color['editor']['fg'],
        borderwidth=0,
        inactive=color['editor']['gutter']['active'],
        block_highlight_text_color=color['syntax']['entity'],
        center_aligned=True,
        fontsize=16,
        **decorations.decor_groupbox
    ),

    widget.TextBox(
        '\uF6D8',
        foreground=color['editor']['indentGuide']['active'],
        fontsize=20,
        **decorations.decor_groupbox
    ),

    widget.Clock(
        format="%-H:%M\n%-d %b %Y",
        **decorations.decor_groupbox
    ),

    widget.Spacer(
        length=bar.STRETCH
    ),

    # Network load segment
    widget.TextBox(
        '\uFBF1',
        fontsize=20,
        **decorations.decor_base
    ),

    widget.Net(
        format='\uE340{down}\n\uE353{up}',
        **decorations.decor_base
    ),

    widget.Spacer(
        length=20
    ),

    # CPU load segment
    widget.TextBox(
        '\uF85A',
        fontsize=20,
        **decorations.decor_base
    ),

    widget.CPU(
        format='{load_percent:>2.0f}%',
        **decorations.decor_base
    ),

    widget.Spacer(
        length=20
    ),

    # Memory segment
    widget.TextBox(
        '\uE266',
        fontsize=20,
        **decorations.decor_base
    ),

    widget.Memory(
        measure_mem='G',
        format='{MemUsed:>2.0f}{mm}',
        **decorations.decor_base
    ),

    widget.Spacer(
        length=20
    ),

    # WiFi segment
    widget.TextBox(
        '\uF96A',
        fontsize=20,
        **decorations.decor_base
    ),

    widget.Wlan(
        format="{percent:2.0%}",
        **decorations.decor_base
    ),

    widget.Spacer(
        length=20
    ),

    # Sound segment
    widget.TextBox(
        '\uFA7D',
        fontsize=20,
        **decorations.decor_base
    ),

    widget.PulseVolume(
        get_volume_command='pamixer --get-volume',
        **decorations.decor_base
    )
]


# Check if backlight exists and add widget
if path.exists('/sys/class/backlight/amdgpu_bl0'):
    widgets.append(
        widget.Spacer(
            length=20
        )
    )

    widgets.append(
        widget.TextBox(
            '\uF5DD',
            fontsize=20,
            **decorations.decor_base
        )
    )

    widgets.append(
        widget.Backlight(
            backlight_name="amdgpu_bl0",
            **decorations.decor_base
        )
    )

# Check if the system has a battery
if path.exists('/sys/class/power_supply/BAT0'):
    widgets.append(
        widget.Spacer(
            length=20
        )
    )

    widgets.append(
        widget.TextBox(
            '\uF578',
            fontsize=20,
            **decorations.decor_base
        )
    )

    widgets.append(
        widget.Battery(
            format="{percent:2.0%}",
            full_char="",
            charge_char="",
            discharge_char="",
            empty_char="",
            unknown_char="",
            low_foreground=color['syntax']['regexp'],
            **decorations.decor_base
        )
    )

# Add final bar padding
widgets.append(
    widget.Spacer(
        length=20
    )
)
