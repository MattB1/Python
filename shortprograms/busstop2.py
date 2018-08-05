#!/usr/bin/env python
"""This is a program to calculate the number or satisfied customers on a bus route"""

#Ask for the bus driver to input the route number
print("Please enter the route number: ")
route_input = input()
route_number = int(route_input)

#Ask the driver to input the number of stope on route
print("Please enter the number of stops along this route: ")
stops_input = input()
number_of_stops = int(stops_input)

#Convert the input to a list
number_of_stops = list(range(number_of_stops))


#Getting number of passengers
on_bus = 0
sum1 = 0
sum2 = 0
passengers_waiting = 0
passengers_leaving = 0
for x in number_of_stops[:]:
	while True:
		try:
			passengers_waiting = int(input("How many passengers are waiting at stop no#", (x)))
		try:
			passengers_leaving = int(input("How many passengers left at stop no#", (x)))
		except:
			pass
		if passengers_waiting < 0:
			print "Please enter a positive number"
			continue
		else:
			break
	while True:
		try:
			passengers_leaving = int(input("How many passengers left the at stop no#", (x)))
		except:
			pass
		if passengers_leaving < 0:
			print "Please enter a positive number"
			continue
		else:
			break

