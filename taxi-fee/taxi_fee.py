#!/usr/bin/env python  
#encoding: utf-8 

def taxi_fee(miles):
	if (miles <= 0):
		return 0
	elif (miles <= 2):
		return 6   
	elif (miles <= 8):
		return round (6 + (miles - 2) * 0.8)
