#!/usr/bin/env python  
#encoding: utf-8 

def taxi_fee(miles, waitminutes): 
	return round(charge_miles(miles) + charge_waitminutes(waitminutes))
  
def charge_miles(miles):  
	valid_miles(miles)

	if (miles == 0):
		return 0
	elif (miles <= 2):
		return 6   
	elif (miles <= 8):
		return 6 + (miles - 2) * 0.8
	else:
		return 6 + (8 - 2) * 0.8 + (miles - 8) *1.2

def charge_waitminutes(waitminutes):
	valid_waitminutes(waitminutes)
	return 0.25 * waitminutes

def valid_miles(miles): 
	if (miles < 0):
		raise invalid_miles

def valid_waitminutes(waitminutes): 
	if (waitminutes < 0):
		raise invalid_waitminutes

class invalid_miles(Exception): "miles should be zero or positive numbers"
class invalid_waitminutes(Exception): "minutes should be zero or positive numbers"