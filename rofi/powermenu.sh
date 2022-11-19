#!/usr/bin/env bash

# Special credit to Aditya Shakya (adi1090x). Some parts here were stolen from Aditya's Rofi theme repo:
# https://github.com/adi1090x/rofi

uptime="`uptime -p | sed -e 's/up //g'`"

# Options
shutdown='襤'
reboot='ﰇ'
lock=''

rofi_cmd() {
    rofi -dmenu \
        -p "I've been awake for $uptime" \
        -mesg "I've been awake for $uptime" \
        -theme ayu_power.rasi
}

run_rofi() {
    echo -e "$lock\n$reboot\n$shutdown\n" | rofi_cmd
}

run_cmd() {
    if [[ $1 == '--shutdown' ]]; then
        systemctl poweroff
    elif [[ $1 == '--reboot' ]]; then
        systemctl reboot
    elif [[ $1 == '--lock' ]]; then
        xsecurelock
    fi
}

chosen="$(run_rofi)"
case ${chosen} in
    $shutdown)
            run_cmd --shutdown
        ;;
    $reboot)
            run_cmd --reboot
        ;;
    $lock)
            run_cmd --lock
        ;;
esac
            
