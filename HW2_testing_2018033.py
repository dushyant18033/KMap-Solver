# CSE 101 - IP HW2
# K-Map Minimization 
# Name: DUSHYANT PANCHAL
# Roll Number: 2018033
# Section: A
# Group: 1
# Date: 12-10-2018

import unittest
from HW2_2018033 import *



class testpoint(unittest.TestCase):
	def test_minFunc(self):
		self.assertEqual(minFunc(3,'(0,1,2,3,4,5,6,7) d -'),"1")
		self.assertEqual(minFunc(3,'() d (0,1,2)'),"0")
		self.assertEqual(minFunc(2,'(0,3) d (2)'),"x' + w")
		self.assertEqual(minFunc(2,'(0) d (1,2)'),"0")
		self.assertEqual(minFunc(4,'(0,1,2,4,5,6,8,9,12,13,14) d -'),"x.z' + w'.z' + y'")
		self.assertEqual(minFunc(4,'(1,3,7,11,15) d (0,2,5)'),"y.z + w'.z OR w'.x' + y.z")
		self.assertEqual(minFunc(3,'(1,3,4,6,7) d -'),"w'.y + x.y + w.y'")
		self.assertEqual(minFunc(3,'(3,4,6,7) d -'),"x.y + w.y'")



if __name__=='__main__':
	unittest.main()
