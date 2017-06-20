import sys
#  data is - +91-9850-kitcat

def is_nondigit(ch):
    if ch.find('+') == 0:
       return False
    if ch.find('-') == 0:
       return False
    if ch.isdigit():
       return False
    return True
fancy_number = sys.argv[1]
print ("Your fancy number is: {}".format(fancy_number))

db =[[1],[2, 'A', 'B', 'C'], [3, 'D', 'E', 'F'], [4, 'G', 'H', 'I'], [5, 'J', 'K', 'L'], [6, 'M', 'N', 'O'], [7, 'P', 'Q', 'R', 'S'], [8,'T', 'U', 'V'], [9, 'W', 'X', 'Y', 'Z']]

non_fancy = ''
for fancy_n in fancy_number:
   fancy_n = fancy_n.upper()
   #print ("I am trying: ", fancy_n)
   if  is_nondigit(fancy_n):
      for d in db:
          if fancy_n in d:
             #print (d[0])
             non_fancy = non_fancy + str(d[0])
   else:
      non_fancy = non_fancy + fancy_n

print ("The non-fancy number is: " + non_fancy)   
