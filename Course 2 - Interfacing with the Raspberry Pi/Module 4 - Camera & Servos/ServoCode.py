#Servo Code

#makes servo go left and right 100 degrees
'Servo Scan Code Example'
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
pwn = GPIO.PWN(12, 50)
pwn.start(0)
for i in range(100):
    pwn.ChangeDutyCycle(i)
    time.sleep(0.1)
for i in range(100, 0, -1):
    pwn.ChangeDutyCycle(i)
    time.sleep(0.1)