#!/usr/bin/python
#--------------------------------------
#    ___  ___  _ ____
#   / _ \/ _ \(_) __/__  __ __
#  / , _/ ___/ /\ \/ _ \/ // /
# /_/|_/_/  /_/___/ .__/\_, /
#                /_/   /___/
#
#       Hall Effect Sensor
#
# This script tests the sensor on GPIO17.
#
# Author   : Matt Hawkins
# Date     : 08/05/2018
# Modified : Dominic Reder
# Date     : 04/03/2019   
#
# https://www.raspberrypi-spy.co.uk/
#
#--------------------------------------

# Import required libraries
import time
import datetime
import RPi.GPIO as GPIO
import BlynkLib
import thread
global blynk

BLYNK_AUTH = 'd9a771bfbfbf41a7b96bc6506b7dfc8a'

blynk = BlynkLib.Blynk(BLYNK_AUTH)


def BlynkLoop():
    global blynk
    print("Blynk thread Started") 
    blynk.run()

pin = 17
trigger = []

def sensorCallback(channel):
  # Called if sensor output changes
  timestamp = time.time()
  stamp = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S:%f')
  if GPIO.input(channel):
    trigger.append(1)
    # No magnet
    print(str(len(trigger)) + " Umdrehung(en) " + stamp)
  else:
    # Magnet
    pass
    #print("Sensor LOW " + stamp)
  return trigger



def main():
  # Wrap main content in a try block so we can
  # catch the user pressing CTRL-C and run the
  # GPIO cleanup function. This will also prevent
  # the user seeing lots of unnecessary error
  # messages.

  # This statement puts Blynk into a thread of its own 
  thread.start_new_thread(BlynkLoop,() )
    
  # Get initial reading
  sensorCallback(pin)

  try:
    # Loop until users quits with CTRL-C
    value=0
    while True :
      time.sleep(0.1)
      blynk.virtual_write(2, (str(len(trigger))))
      

  except KeyboardInterrupt:
    # Reset GPIO settings
    GPIO.cleanup()

# Tell GPIO library to use GPIO references
GPIO.setmode(GPIO.BCM)
#print("Setup GPIO pin as input on GPIO17")

# Set Switch GPIO as input
# Pull high by default
GPIO.setup(pin , GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(pin, GPIO.BOTH, callback=sensorCallback, bouncetime=100)

if __name__=="__main__":
   main()
