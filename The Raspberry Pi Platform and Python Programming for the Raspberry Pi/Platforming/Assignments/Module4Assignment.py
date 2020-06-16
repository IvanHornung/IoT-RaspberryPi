import Rpi.Gpio as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)
GPIO.setup(7, GPIO.OUT)

GPIO.output(7, False)

while True:
  if GPIO.input(11):
      GPIO.output(7, False)
  else:
    GPIO.output(7, True)
      time.sleep(0.25)
    GPIO.output(7, True)
      time.sleep(0.25)
