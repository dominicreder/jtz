#!/bin/sh
# Start Script für den Biker
export PATH=$PATH:/opt/nodejs/bin/
unset NODE_PATH

cd /home/pi/Projekte/jtz/

blynk-client QlvbwgyTZXh74m8dz5E6MUNAFpFKmQ3W &

python biker.py
