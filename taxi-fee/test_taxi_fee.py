#!/usr/bin/env python  
#encoding: utf-8  
  
import unittest  
from taxi_fee import taxi_fee
  
class test_(unittest.TestCase):  
      
    def setUp(self):  
        pass   
    
    def tearDown(self):  
        pass        

    def test_given_0miles_should_charge_0(self):  
        self.assertEqual(taxi_fee(0,0), 0) 

    def test_given_less_than_2miles_should_charge_6(self):  
        self.assertEqual(taxi_fee(1,0), 6)

    def test_given_equals_to_2miles_should_charge_6(self):  
        self.assertEqual(taxi_fee(2,0), 6)

    def test_given_greater_than_2miles_but_less_than_8miles_should_charge_6_plus_8mao_per_mile_then_round(self):  
        self.assertEqual(taxi_fee(4,0), round (6 + (4-2) * 0.8))

    def test_given_equals_to_8miles_should_charge_6_plus_8mao_per_mile_then_round(self):  
        self.assertEqual(taxi_fee(8,0), round (6 + (8-2) * 0.8))      

    def test_given_greater_than_8miles_should_charge_4mao_more_per_mile_for_greater_parts_then_round(self):  
        self.assertEqual(taxi_fee(9,0), round (6 + (8-2) * 0.8 + (9-8) * 1.2))


if __name__ =='__main__':  
    unittest.main() 