# Disable beep
xset -b

# Start Pulseaudio Daemon
#pulseaudio -D &

# Start compositor for fancy visuals
picom --backend glx --fade-exclude 'class_g = "xsecurelock"' &

# Unclutter - hide the mouse cursor
unclutter --jitter 10 --ignore-scrolling --start-hidden --fork

# Nitrogen for wallpaper
# nitrogen --set-zoom-fill ~/Pictures/wallpaper.jpg &

# Set xsecurelock environment variables
export XSECURELOCK_PASSWORD_PROMPT=asterisks

# Set lock screen autolock
xset s 300 5
xss-lock -n /usr/lib/xsecurelock/dimmer -l -- xsecurelock &

# Start qtile window manager
qtile start
