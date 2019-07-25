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
import blynklib
import thread


BLYNK_AUTH = 'dd1548f71daa4e81ad4e3238069b2f62'

blynk = blynklib.Blynk(BLYNK_AUTH)


def BlynkLoop():
    global blynk
    print("Blynk thread Started") 
    blynk.run()

pin = 17

def sensorCallback(channel):
  global sensorCounter
  global sensorStatus
  sensorStatus = True
  # Called if sensor output changes
  timestamp = time.time()
  stamp = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S:%f')
  sensorCounter += 1
  print "Sensor LOW " + stamp


def main():
  # Wrap main content in a try block so we can
  # catch the user pressing CTRL-C and run the
  # GPIO cleanup function. This will also prevent
  # the user seeing lots of unnecessary error
  # messages.

  # This statement puts Blynk into a thread of its own 
  thread.start_new_thread(BlynkLoop,() )

  try:
    global sensorCounter
    global sensorStatus
    sensorStatus = True
    sensorCounter = 0
    # Loop until users quits with CTRL-C

    while True :
      if sensorStatus == True:
        print "Sensor Counter " , sensorCounter
        sensorStatus = False
      time.sleep(0.05)
      blynk.virtual_write(2, sensorCounter)
      

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
