import RPi.GPIO as GPIO                    #Import GPIO library
import time
import atexit
import datetime
from firebase import firebase
import urllib2, urllib, httplib
import json
import os
from functools import partial                               
GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering 
firebase = firebase.FirebaseApplication('https://smart-stick-ea013.firebaseio.com')
TRIG = 20                                  #Associate pin 38 to TRIG
ECHO = 26                                  #Associate pin 37 to ECHO
TRIG2 = 16							#Associate pin 36 to TRGI2
ECHO2 = 19                					#Associate pin 35 to ECHO2

print "Measuring Distance"

GPIO.setup(TRIG,GPIO.OUT)           #Sensor1 #Set pin as GPIO out
GPIO.setup(ECHO,GPIO.IN)                   #Set pin as GPIO in
GPIO.setup(TRIG2.GPIO.OUT)			#Sensor2 #Set pin as GPIO out
GPIO.setup(ECHO2.GPIO.IN)				   #Set pin as GPIO in

while True:

  #Sensor 1
  GPIO.output(TRIG, False)                 #Set TRIG as LOW
  print "Waiting For Sensor To Settle"
  time.sleep(2)                            #Delay of 2 seconds

  GPIO.output(TRIG, True)                  #Set TRIG as HIGH
  time.sleep(0.00001)                      #Delay of 0.00001 seconds
  GPIO.output(TRIG, False)                 #Set TRIG as LOW

  while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
    pulse_start = time.time()              #Saves the last known time of LOW pulse

  while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
    pulse_end = time.time()                #Saves the last known time of HIGH pulse 

  pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

  distance1 = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
  distance1 = round(distance1, 2)            #Round to two decimal points
  
  #Sensor 2
  GPIO.output(TRIG2, False)                 #Set TRIG as LOW
  print "Waiting For Sensor To Settle"
  time.sleep(2)                            #Delay of 2 seconds

  GPIO.output(TRIG2, True)                  #Set TRIG as HIGH
  time.sleep(0.00001)                      #Delay of 0.00001 seconds
  GPIO.output(TRIG2, False)                 #Set TRIG as LOW

  while GPIO.input(ECHO2)==0:               #Check whether the ECHO is LOW
    pulse_start2 = time.time()              #Saves the last known time of LOW pulse

  while GPIO.input(ECHO2)==1:               #Check whether the ECHO is HIGH
    pulse_end2 = time.time()                #Saves the last known time of HIGH pulse 

  pulse_duration2 = pulse_end2 - pulse_start2 #Get pulse duration to a variable

  distance2 = pulse_duration2 * 17150        #Multiply pulse duration by 17150 to get distance
  distance2 = round(distance2, 2)            #Round to two decimal points
  
  #Comparing 2 sensor's distance
  if distance1 < distance2 and distance1 < 400:      #Check whether the distance is within range
    print "Distance:",distance1 - 0.5,"cm"  #Print distance with 0.5 cm calibration
    firebase.put('Sensors/sensor1',"distance",distance1) #Other_method #firebase.post('/Sensors/sensor1', distance)
  elif distance2 < distance1 and distance2 < 400:
    print "Distance:",distance2 - 0.5,"cm"  #Print distance with 0.5 cm calibration
    firebase.put('Sensors/sensor1',"distance",distance2)  #firebase.post('/Sensors/sensor1', distance)
  else:
    print "Out Of Range"                   #display out of range
