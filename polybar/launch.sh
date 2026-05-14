#!/bin/bash

# Mata qualsevol polybar que ja estigui corrent
killall -q polybar

# Llança la nostra barra
polybar mybar &
