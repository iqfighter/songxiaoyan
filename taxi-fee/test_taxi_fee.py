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
        self.assertEqual(taxi_fee(0), 0) 

    def test_given_less_than_2miles_should_charge_6(self):  
        self.assertEqual(taxi_fee(1), 6)

if __name__ =='__main__':  
    unittest.main() 