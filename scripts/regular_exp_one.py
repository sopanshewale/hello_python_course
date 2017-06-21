import sys
import re

regex = sys.argv[1]

while True:
    s = raw_input()
    m = re.search(regex, s)
    if m: 
       print (s)
    else:
       pass
  
