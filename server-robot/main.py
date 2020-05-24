#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

import socket

# Initialize motors
cMotor = Motor(Port.C)
dMotor = Motor(Port.D)
robot = DriveBase(cMotor, dMotor, 56, 60)

aMotor = Motor(Port.A, Direction.CLOCKWISE, [1, 24])

s = socket.socket()
print("Socket successfully created")

port = 12345

s.bind(('', port))
print("socket bound to {}".format(port))

s.listen(5)
print("socket is listening")

connect, addr = s.accept()
print("Got connection from {}".format(addr))

turnSharpness = 100
TravelTime = 300

while True:
#for i in range(0, 5):
    rawByte = connect.recv(1)
    print("Client sent: {}".format(rawByte))
    decodedStr = rawByte.decode('utf-8')
    print("Decoded str: {}".format(decodedStr))
    if decodedStr == "q":
		print(" Client is done!")
		break
    if decodedStr == "i":
        #cMotor.run_target(500, 180, Stop.COAST, False)
        #dMotor.run_target(500, 180, Stop.COAST, False)
        brick.display.image(ImageFile.UP)
        brick.light(Color.GREEN)
        robot.drive(100, 0)

    if decodedStr == "k":
        #cMotor.run_target(500, -180, Stop.COAST, False)
        #dMotor.run_target(500, -180, Stop.COAST, False)
        brick.display.image(ImageFile.DOWN)
        brick.light(Color.ORANGE)
        robot.drive(-100, 0)

    if decodedStr == "j":
        brick.display.image(ImageFile.MIDDLE_LEFT)
        brick.light(Color.YELLOW)
        robot.drive(100, -turnSharpness)

    if decodedStr == "l":
        brick.display.image(ImageFile.MIDDLE_RIGHT)
        brick.light(Color.YELLOW)
        robot.drive(100, turnSharpness)

    if decodedStr == "z":
        aMotor.run_time(100, 1000, Stop.COAST, False)

    if decodedStr == "x":
        aMotor.run_time(-100, 1000, Stop.COAST, False)

    wait(TravelTime)
    robot.stop(Stop.COAST)

#close connection with laptop
connect.close()