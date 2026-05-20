#!/bin/bash

echo "=============================="
echo " Instal·lant entorn personalitzat"
echo "=============================="

# Instal·la els paquets necessaris
sudo apt update
sudo apt install -y qtile polybar rofi git feh xterm

# Crea les carpetes de configuració
mkdir -p /home/$USER/.config/qtile
mkdir -p /home/$USER/.config/polybar
mkdir -p /home/$USER/.config/rofi

# Copia els fitxers de configuració
cp ./qtile/config.py /home/$USER/.config/qtile/config.py
cp ./polybar/config.ini /home/$USER/.config/polybar/config.ini
cp ./polybar/launch.sh /home/$USER/.config/polybar/launch.sh
cp ./rofi/config.rasi /home/$USER/.config/rofi/config.rasi
cp ./wallpaper.jpg /home/$USER/wallpaper.jpg

echo "=============================="
echo " Fet! Reinicia sessió i selecciona Qtile."
echo "=============================="
