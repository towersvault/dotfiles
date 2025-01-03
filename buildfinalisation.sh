#!/bin/sh

pacman -Syu

# Install YAY
pacman -S --needed git base-devel
cd /opt
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si

# Install clight
yay -S clight

# Install nerd-fonts
pacman -S nerd-fonts

# Install hyprland
pacman -S hyprland 