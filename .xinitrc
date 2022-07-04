# Disable beep
xset -b

# Start Pulseaudio Daemon
pulseaudio -D &

# Start compositor for fancy visuals
picom &

# Unclutter - hide the mouse cursor
unclutter --jitter 10 --ignore-scrolling --start-hidden --fork

# Nitrogen for wallpaper
# nitrogen --set-zoom-fill ~/Pictures/wallpaper.jpg &

# Start qtile window manager
qtile start
