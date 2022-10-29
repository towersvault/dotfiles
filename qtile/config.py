# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.widget import backlight

from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration

from keybinds import keys
from layouts import layouts
from groups import groups
from colors import ayu_dark as color
import decorations


mod = "mod4"
terminal = guess_terminal("alacritty")


widget_defaults = dict(
    font="Source Code Pro Black, NotoEmoji Nerd Font Mono",
    fontsize=12,
    padding=0,
    foreground=color['editor']['fg'],
    background=color['ui']['bg']
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(
                    '\uf303',
                    foreground=color['syntax']['tag'],
                    fontsize=16,
                    **decorations.decor_base
                ),

                # Group box segment
                widget.GroupBox(
                    highlight_method="font",
                    active=color['editor']['gutter']['active'],
                    borderwidth=0,
                    inactive=color['editor']['indentGuide']['active'],
                    block_highlight_text_color=color['syntax']['tag'],
                    center_aligned=True,
                    fontsize=14,
                    **decorations.decor_base
                ),

                widget.Spacer(
                    length=16
                ),

                # Prompt segment
                widget.Prompt(
                    prompt='\uF848 ',
                    foreground=color['ui']['line'],
                    **decorations.decor_prompt
                ),

                widget.Spacer(
                    length=16
                ),

                # Window name segment
                widget.WindowName(),

                widget.Spacer(),

                # WiFi segment
                widget.TextBox(
                    'WLAN',
                    **decorations.decor_widget_title
                ),

                widget.Wlan(
                    format="{essid} {percent:2.0%}",
                    **decorations.decor_base
                ),

                widget.Spacer(
                    length=16
                ),

                # Sound segment
                widget.TextBox(
                    'VOLM',
                    **decorations.decor_widget_title
                ),
                
                widget.PulseVolume(
                    **decorations.decor_base
                ),

                widget.Spacer(
                    length=16
                ),

                # Brightness segment
                widget.TextBox(
                    'BCKL',
                    **decorations.decor_widget_title
                ),

                widget.Backlight(
                    backlight_name="amdgpu_bl0",
                    **decorations.decor_base
                ),

                widget.Spacer(
                    length=16
                ),

                # Battery segment
                widget.TextBox(
                    'BATT',
                    **decorations.decor_widget_title
                ),
                
                widget.Battery(
                    format="{char}{percent:2.0%}",
                    full_char="",
                    charge_char="\uf0e7 ",
                    discharge_char="",
                    empty_char="",
                    unknown_char="",
                    low_foreground=color['syntax']['regexp'],
                    **decorations.decor_base
                ),

                widget.Spacer(
                    length=16
                ),

                # Clock segment
                widget.TextBox(
                    'TIME',
                    **decorations.decor_widget_title
                ),
                
                widget.Clock(
                    format="%-H:%M",
                    **decorations.decor_base
                ),

                widget.Spacer(
                    length=16
                ),

                widget.TextBox(
                    '\uF444',
                    fontsize=26,
                    foreground=color['common']['accent'],
                    mouse_callbacks={lazy.spawn('systemctl hibernate')},
                    **decorations.decor_power
                ),

                widget.TextBox(
                    '\uF444',
                    fontsize=26,
                    foreground=color['common']['error'],
                    mouse_callbacks={lazy.spawn('systemctl poweroff')},
                    **decorations.decor_power
                ),

                widget.Spacer(
                    length=16
                )
            ],

            # Height of Bar
            40,

            # Margin
            margin=[0, 0, 0, 0],

            opacity=1
        ),
        # Set Static Wallpaper
        wallpaper="/home/clifford/Downloads/sebastian-staines-O5rFo-cJu94-unsplash.jpg",

        # Wallpaper mode to 'fill' or 'stretch'
        wallpaper_mode='fill'
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_normal=color['editor']['bg'],
    border_focus=color['editor']['fg'],
    border_width=0,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
