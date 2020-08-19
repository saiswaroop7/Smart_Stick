import RPi.GPIO as GPIO
from time import sleep
import datetime
from firebase import firebase
import urllib2, urllib, httplib
import json
import os
from functools import partial

firebase = firebase.FirebaseApplication('https://smart-stick-65e06.firebaseio.com', None);

firebase.post('/sensor/', distance)


firebase.delete('/users', '1')
