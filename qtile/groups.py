from libqtile.config import Group, Key
from libqtile.lazy import lazy

from keybinds import keys


mod = 'mod4'

# groups = [Group(i) for i in "123456789"]
groups = list()
groups.append(Group('1', label='\uF738'))  # Firefox
groups.append(Group('2', label='\uE795'))  # Terminal
groups.append(Group('3', label='\uFB0F'))  # VSCode
# groups.append(Group(''))  # IntelliJ IDEA
groups.append(Group('4', label='\uF9C6'))  # Spotify 
groups.append(Group('5', label='\uF1B6'))  # Steam
groups.append(Group('6', label='\uE7B5'))  # IntelliJ
groups.append(Group('7', label='\uF860'))  # Chat Apps
groups.append(Group('8', label='\uF718'))  # Office
groups.append(Group('9', label='\uF444'))  # Generic

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