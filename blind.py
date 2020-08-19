# Import the Raspberry pi GPIO module.
import RPi.GPIO as GPIO
GPIO.setwarnings(False) # supress the system wornings
GPIO.cleanup() # clean up the GPIO pins i.e make the GPIO pins to low
# Set the mode of numbering the pins.
GPIO.setmode(GPIO.BOARD)
#function to call festival TTS system
def speak(text):
from subprocess import PIPE, Popen
process = Popen(['festival', '--tts'], stdin=PIPE)
process.stdin.write(text + '\n')
process.stdin.close()
process.wait()
GPIO.setup(11, GPIO.IN)
#GPIO pin 11 is the input.
GPIO.setup(12, GPIO.IN)
#GPIO pin 12 as input
GPIO.setup(13, GPIO.IN)
#GPIO pin 13 as input pin
left = GPIO.input(11)
fornt = GPIO.input(12)
right = GPIO.input(13)
#keep on polling for input pins
while 1:
left = GPIO.input(11)
front = GPIO.input(12)
right = GPIO.input(13)
if left == True or front == True or right == True:
if left == False and front == False and right == True:
speak("move either left ot front")
elif left == False and front == True and right == False:
speak("move either left or right")
elif left == False and front == True and right == True:
speak("move left")
elif left == True and front == False and right == False:
speak("move either front or right")
elif left == True and front == False and right == True:
speak("move front")
elif left == True and front == True and right == False:
speak("move right")
elif left == True and front == True and right == True:
speak("better to go back")
else:
speak("you can move in any direction")