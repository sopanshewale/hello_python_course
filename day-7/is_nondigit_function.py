import sys
import re


pattern = re.compile('[-\d\+]')

def is_nondigit(ch):
     m = re.search(pattern, ch)
     if m: 
         return False
     else:
         return True
 

my_number = sys.argv[1]

if is_nondigit(my_number):
     print ("Not a number:", my_number)
else:
     print ("It's number:", my_number)

