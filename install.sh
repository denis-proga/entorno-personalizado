#!/bin/bash

echo "=============================="
echo " Instal·lant entorn personalitzat"
echo "=============================="

# Instal·la els paquets necessaris
sudo apt update
sudo apt install -y qtile polybar rofi git python3 feh xterm

# Crea les carpetes de configuració
mkdir -p ~/.config/qtile
mkdir -p ~/.config/polybar
mkdir -p ~/.config/rofi

# Copia els fitxers de configuració
cp ./qtile/config.py ~/.config/qtile/config.py
cp ./polybar/config.ini ~/.config/polybar/config.ini
cp ./polybar/launch.sh ~/.config/polybar/launch.sh
cp ./rofi/config.rasi ~/.config/rofi/config.rasi

# Dona permisos a polybar
chmod +x ~/.config/polybar/launch.sh

echo "=============================="
echo " Fet! Reinicia sessió per aplicar."
echo "=============================="
