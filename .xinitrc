# Disable beep
xset -b

# Start Pulseaudio Daemon
# pulseaudio -D &

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

# Cursor changes
xinput --set-prop 13 'libinput Accel Profile Enabled' 0, 1  # Disable mouse acceleration
xinput set-button-map 13 1 1 3 4 5 6 7  # Disable middle mouse click
xinput --set-prop 13 'libinput Accel Speed' 0.7  # Set cursor speed

# Set Dolphin icons
export QT_QPA_PLATFORMTHEME=qt5ct

# Start qtile window manager
qtile start
