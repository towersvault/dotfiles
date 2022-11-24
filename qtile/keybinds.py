"""
Mouse and keyboard bindings.
"""


from libqtile.lazy import lazy
from libqtile.config import Key
from libqtile.utils import guess_terminal

from datetime import datetime

from utils import get_next_screenshot_new as get_next_screenshot


mod = 'mod4'
terminal = guess_terminal('alacritty')

keys = [
    # Move window focus
    Key([mod], 'Left', lazy.layout.left(), desc='Move focus to left'),
    Key([mod], 'Right', lazy.layout.right(), desc='Move focus to right'),
    Key([mod], 'Down', lazy.layout.down(), desc='Move focus down'),
    Key([mod], 'Up', lazy.layout.up(), desc='Move focus up'),

    # Move windows around the current group
    Key([mod, 'shift'], 'Left', lazy.layout.shuffle_left(), desc='Move window to the left'),
    Key([mod, 'shift'], 'Right', lazy.layout.shuffle_right(), desc='Move window to the right'),
    Key([mod, 'shift'], 'Down', lazy.layout.shuffle_down(), desc='Move window to the bottom'),
    Key([mod, 'shift'], 'Up', lazy.layout.shuffle_up(), desc='Move window to the top'),

    # Grow focused window in the chosen direction
    Key([mod, 'control'], 'Left', lazy.layout.grow_left(), desc='Grow window to the left'),
    Key([mod, 'control'], 'Right', lazy.layout.grow_right(), desc='Grow window to the right'),
    Key([mod, 'control'], 'Down', lazy.layout.grow_down(), desc='Grow window down'),
    Key([mod, 'control'], 'Up', lazy.layout.grow_up(), desc='Grow window up'),
    Key([mod], 'n', lazy.layout.normalize(), desc='Reset all window sizes'),

    # Close focused window
    Key([mod], 'q', lazy.window.kill(), desc='Close the focused window'),

    # Lock computer
    Key([mod, 'shift'], 'q', lazy.spawn('xset s activate')),

    # Show power menu
    Key([mod], 'Escape', lazy.spawn('/home/clifford/dotfiles/rofi/powermenu.sh')),

    # Spawn terminal
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Spawn application
    Key([mod, 'shift'], 'space', lazy.spawncmd(), desc='Spawn a command using a prompt widget'),
    Key([mod], 'space', lazy.spawn('rofi -disable-history -drun-display-format {name} -show drun')),

    # Reload config
    Key([mod, 'control'], 'r', lazy.reload_config(), desc='Reload the config'),

    # Shutdown Qtile
    Key([mod, 'control'], 'q', lazy.shutdown(), desc='Shutdown Qtile'),

    # Media keys
    Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 2")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 2")),

    Key([], "XF86AudioPlay", lazy.spawn("playerctl -i 'firefox' play-pause")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl -i 'firefox' stop")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl -i 'firefox' next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl -i 'firefox' previous")),

    # Brightness keys
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +5%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-")),

    # Screenshot
    Key([], "Print", lazy.spawn(f"scrot 'Screenshot_%Y%m%d_%H%M%S.png' -e 'mv $f $$(xdg-user-dir SCREENSHOTS)'")),

    # Change layouts
    Key([mod], 'Tab', lazy.window.toggle_floating(), desc='Toggle highlighted window to either floating or non-floating, opposite of which it is')
]