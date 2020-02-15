#!/bin/sh
# Start Script für den Biker
export PATH=$PATH:/opt/nodejs/bin/
unset NODE_PATH
blynk-client fca768ffc1d74bc68fa9aca217c90f46 &
cd ~/Projekte/jtz/
python biker.py
