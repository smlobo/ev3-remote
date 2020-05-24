#!/usr/local/bin/python3

import socket
import time

import sys
import tty
import termios

# Read a key press from the keyboard, return the ASCII character
def readKey():
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	return ch

# Create a socket
clientSocket = socket.socket()

# IP address of the robot
ipAddress = "192.168.1.98"

# Port number to connect to
port = 12345

# Connect to the robot (server)
clientSocket.connect((ipAddress, port))
print("Connected to robot: {} : {}".format(ipAddress, port))

# Loop until the 'q' key is pressed
while True:
	character = readKey()
	print("Sending: {}".format(character))
	clientSocket.send(bytes([ord(character)]))
	if character == 'q':
		print("We are done - quitting!")
		break

# Terminate the connection
clientSocket.close()
