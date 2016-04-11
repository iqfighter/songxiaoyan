#!/usr/bin/env python  
#encoding: utf-8 

def taxi_fee(miles, waitminutes):  
	return round(charge_miles(miles) + charge_waitminutes(waitminutes))
  
def charge_miles(miles):  
	if (miles <= 0):
		return 0
	elif (miles <= 2):
		return 6   
	elif (miles <= 8):
		return 6 + (miles - 2) * 0.8
	else:
		return 6 + (8 - 2) * 0.8 + (miles - 8) *1.2

def charge_waitminutes(minutes):
	return 0.25 * minutes