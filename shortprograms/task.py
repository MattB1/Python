#!/usr/bin/env Python3

#Ask user to enter age in years
age_in_years = input("Enter your age in years")
age_in_years = int(age_in_years)


#calculate how many years until they reach 100

#Options

if age_in_years >= 100:
	print("You've already turned 100")


elif age_in_years < 0 :
	print("Try again after your born")


else :
	print (100 - age_in_years)


#If they are older than 100 they will get a message saying "You've already turned 100"

#If they are less than 0 they will get a message saying "Try again after your born"

#
