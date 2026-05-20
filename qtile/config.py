from libqtile import layout, bar, widget, hook
from libqtile.config import Key, Group, Screen
from libqtile.lazy import lazy

# Tecla principal (Super = tecla Windows)
mod = "mod4"

# ============ SHORTCUTS ============
keys = [
    # Moure el focus entre finestres
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),

    # Obrir terminal
    Key([mod], "Return", lazy.spawn("xterm")),

    # Obrir menú d'aplicacions (rofi)
    Key([mod], "r", lazy.spawn("rofi -show drun")),

    # Tancar finestra
    Key([mod], "q", lazy.window.kill()),

    # Reiniciar Qtile
    Key([mod, "control"], "r", lazy.restart()),

    # Sortir de Qtile
    Key([mod, "control"], "q", lazy.shutdown()),
]

# ============ ESCRITORIOS (workspaces) ============
groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        # Super + número = anar a l'escriptori
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        # Super + Shift + número = moure finestra a l'escriptori
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])

# ============ LAYOUTS (distribució de finestres) ============
layouts = [
    layout.Columns(border_focus="#00BFFF", border_width=2),
    layout.Max(),
]

# ============ BARRA SUPERIOR ============
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(),           # Mostra els escriptoris
                widget.Spacer(),             # Espai en blanc
                widget.Clock(               # Rellotge
                    format="%d/%m/%Y %H:%M"
                ),
            ],
            24,                             # Alçada de la barra
            background="#1e1e2e",           # Color de fons
        ),
    ),
]

# Layout per defecte
main = None
follow_mouse_focus = True
cursor_warp = False

import subprocess

@hook.subscribe.startup_once
def autostart():
	subprocess.Popen(['feh', '--bg-scale', '/home/denis/wallpaper.jpg'])
