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
import colors
import colors2
import decorations


mod = "mod4"
terminal = guess_terminal("alacritty")


""" groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    ) """

widget_defaults = dict(
    font="NotoSans, NotoEmoji Nerd Font Mono",
    fontsize=12,
    padding=0,
    foreground=colors2.SUBTEXT_1,
    background=colors2.CRUST
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.Spacer(
                    length=16
                ),

                # Group box segment
                widget.GroupBox(
                    highlight_method="font",
                    active=colors2.SURFACE_1,
                    borderwidth=0,
                    inactive=colors2.BASE,
                    block_highlight_text_color=colors2.TEXT,
                    center_aligned=True,
                    **decorations.decor_base
                ),

                widget.Spacer(
                    length=16
                ),

                # Prompt segment
                widget.Prompt(
                    prompt='\uF848 ',
                    foreground=colors2.CRUST,
                    **decorations.decor_prompt
                ),

                widget.Spacer(
                    length=16
                ),

                # Window name segment
                widget.WindowName(
                    foreground=colors2.SUBTEXT_0
                ),

                widget.Spacer(),

                # WiFi segment
                widget.TextBox(
                    "\uF09E",
                    foreground=colors2.TEXT,
                    **decorations.decor_wifi
                ),
                widget.Spacer(
                    length=4
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
                    "\uFA7D",
                    foreground=colors2.TEXT,
                    **decorations.decor_sound
                ),
                widget.Spacer(
                    length=4
                ),
                widget.Volume(
                    **decorations.decor_base
                ),

                widget.Spacer(
                    length=16
                ),

                # Brightness segment
                widget.TextBox(
                    "\uFC6A",
                    foreground=colors2.TEXT,
                    **decorations.decor_brightness
                ),
                widget.Spacer(
                    length=4
                ),
                widget.Backlight(
                    backlight_name="amdgpu_bl0",
                    **decorations.decor_base
                ),

                widget.Spacer(
                    length=16
                ),

                # Battery segment
                widget.Battery(
                    format="{char}",
                    foreground=colors2.TEXT,
                    full_char="\uF578",
                    charge_char="\uF583",
                    discharge_char="\uF58B",
                    empty_char="\uF582",
                    unknown_char="\uF578",
                    **decorations.decor_battery
                ),
                widget.Spacer(
                    length=4
                ),
                widget.Battery(
                    format="{percent:2.0%}",
                    full_char="\uF578",
                    charge_char="\uF583",
                    discharge_char="\uF58B",
                    empty_char="\uF582",
                    unknown_char="\uF578",
                    **decorations.decor_base
                ),

                widget.Spacer(
                    length=16
                ),

                # Clock segment
                widget.TextBox(
                    "\uF64F",
                    foreground=colors2.TEXT,
                    **decorations.decor_clock
                ),
                widget.Spacer(
                    length=4
                ),
                widget.Clock(
                    format="%-H:%M",
                    **decorations.decor_base
                ),

                widget.Spacer(
                    length=16
                ),

                # Systray segment
                widget.Systray(),
            ],
            40,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # Set Static Wallpaper
        wallpaper="/home/clifford/Pictures/archlinux-wallpaper.png",

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
