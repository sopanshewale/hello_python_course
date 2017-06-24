import re
import sys

pattern  = re.compile('[-\d+]')

def is_nondigit(ch):
    m = re.search(pattern, ch)
    if m:
      return False
    else: 
      return True


if is_nondigit(sys.argv[1]):
   print ("The charector is not digit: {}".format(sys.argv[1]))
else:  
   print ("The charector is digit: {}".format(sys.argv[1]))
