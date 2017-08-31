'''
File: Velocity&YawCtrl.py
Author: Roger Wang
Description: This file is an example for a basic practice to command the drone to 
             takeoff, control its velocity, yaw orientation and land.           
'''

import FlightController
import sys
import time

# Create a Vehicle object
myCopter = FlightController.Vehicle()

# Connect and initialize the vehicle, enable SITL here
if not myCopter.initialize(simulation = True):
	sys.exit(1)

# Try arming the vehicle
timeoutCounter = 0
while not myCopter.arm():
	timeoutCounter += 1
	if timeoutCounter > 3:
		print "Cannot arm the vehicle after 3 retries."
		sys.exit(1)

# Takeoff
if not myCopter.takeoff(1):
	sys.exit(1)

# Hover for 5 seconds
time.sleep(5)

# Go westward at 1m/s for 5 seconds
print "Going westward at 1m/s for 5s"
myCopter.send_nav_velocity(0, -1, 0)
time.sleep(5)

# Hover for 5 seconds
print "Hovering"
myCopter.send_nav_velocity(0, 0, 0)
time.sleep(5)

# Change yaw direction to (0, north) and wait for 5 seconds
print "Change the vehicle direction to north"
myCopter.condition_yaw(0)
time.sleep(5)

# Change yaw direction to (90, east) and wait for 5 seconds
print "Change the vehicle direction to east"
myCopter.condition_yaw(90)
time.sleep(5)

# Go northward at 1m/s for 5 seconds
print "Going northward at 1m/s for 5s"
myCopter.send_nav_velocity(1, 0, 0)
time.sleep(5)

# Without hovering, go upward at 0.2m/s for 5 seconds
print "Going upward for 0.2m/s for 5 seconds"
myCopter.send_nav_velocity(0, 0, -0.2)
time.sleep(5)

# Hover for 5 seconds
print "Hovering"
myCopter.send_nav_velocity(0, 0, 0)
time.sleep(5)

# Land
timeoutCounter = 0
while not myCopter.land():
	timeoutCounter += 1
	if timeoutCounter > 3:
		print "Critical: Cannot land the vehicle after 3 retries."
		sys.exit(1)
		
myCopter.exit()