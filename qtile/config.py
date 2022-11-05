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
    foreground=color['editor']['fg']
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
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

                # Group box segment
                widget.GroupBox(
                    highlight_method="font",
                    active=color['editor']['fg'],
                    borderwidth=0,
                    inactive=color['editor']['gutter']['normal'],
                    block_highlight_text_color=color['syntax']['entity'],
                    center_aligned=True,
                    fontsize=16,
                    **decorations.decor_groupbox
                ),

                widget.Clock(
                    format="%-H:%M\n%-d %b %Y",
                    **decorations.decor_groupbox
                ),

                widget.Spacer(
                    length=bar.STRETCH
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
                    **decorations.decor_base
                ),

                widget.Spacer(
                    length=20
                ),

                # # Brightness segment
                widget.TextBox(
                    '\uF5DD',
                    fontsize=20,
                    **decorations.decor_base
                ),

                widget.Backlight(
                    backlight_name="amdgpu_bl0",
                    **decorations.decor_base
                ),

                widget.Spacer(
                    length=20
                ),

                # Battery segment
                widget.TextBox(
                    '\uF578',
                    fontsize=20,
                    **decorations.decor_base
                ),
                
                widget.Battery(
                    format="{percent:2.0%}",
                    full_char="",
                    charge_char="",
                    discharge_char="",
                    empty_char="",
                    unknown_char="",
                    low_foreground=color['syntax']['regexp'],
                    **decorations.decor_base
                ),

                widget.Spacer(
                    length=20
                )
            ],

            # Height of Bar
            50,

            # Margin
            margin=[0, 0, 0, 0],

            background=color['ui']['bg']
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
