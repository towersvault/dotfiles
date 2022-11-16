from libqtile.config import Group, Key
from libqtile.lazy import lazy

from keybinds import keys


mod = 'mod4'

group_attributes = (
    {
        'label': '\uF738',  # Firefox
        'color': ''
    },
    {
        'label': '\uE795',  # Terminal
        'color': ''
    },
    {
        'label': '\uFB0F',  # VSCode
        'color': ''
    },
    {
        'label': '\uF9C6',  # Spotify
        'color': ''
    },
    {
        'label': '\uF1B6',  # Steam
        'color': ''
    },
    {
        'label': '\uE7B5',  # IntelliJ
        'color': ''
    },
    {
        'label': '\uF860',  # Chat Apps
        'color': ''
    },
    {
        'label': '\uF48A',  # Office
        'color': ''
    },
    {
        'label': '\uF444',  # Generic
        'color': ''
    },
)

groups = [Group(str(i + 1), label=group_attributes[i]['label']) for i in range(0, len(group_attributes))]

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
    )