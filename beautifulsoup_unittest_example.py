# Program to print
#   1) Last 3 link's text on webpage
#   2) Test Max and Min prices on the page using unittest
#   3) Using 

import urllib3
http = urllib3.PoolManager()
from bs4 import BeautifulSoup
import unittest

r = http.request('GET', 'http://www.dollar2rupee.net/')
soup = BeautifulSoup(r.data,"lxml") 
tds = soup.find_all("td")
prices =[]

for td in tds:
	if len(td.text) == 5:
		prices.append(td.text)

print prices
print '\n'.join(prices) #pretty print list by converting it to a string
max_price = max(prices)
min_price = min(prices)
print 'max price is: ',max_price
print 'min price is: ',min_price


class MyTest(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max_price, '66.62')
    def test_min(self):
        self.assertEqual(min_price, '66.01')    

if __name__ == '__main__':
    unittest.main()      

'''
[u'66.61', u'66.40', u'66.01', u'66.48', u'66.03', u'66.50', u'66.03', u'66.09', u'66.45', u'66.50']
66.61
66.40
66.01
66.48
66.03
66.50
66.03
66.09
66.45
66.50
max price is:  66.61
min price is:  66.01
F.
======================================================================
FAIL: test_max (__main__.MyTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\pinup\Desktop\code\node-course\beautifulsoup_unittest_example.py", line 30, in test_max
    self.assertEqual(max_price, '66.62')
AssertionError: u'66.61' != '66.62'

----------------------------------------------------------------------
Ran 2 tests in 0.001s
'''  

