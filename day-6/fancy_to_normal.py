import sys
#  data is - +91-9850-kitcat

fancy_number = sys.argv[1]
print ("Your fancy number is: {}".format(fancy_number))

db =[[1],[2, 'A', 'B', 'C'], [3, 'D', 'E', 'F'], [4, 'G', 'H', 'I'], [5, 'J', 'K', 'L'], [6, 'M', 'N', 'O'], [7, 'P', 'Q', 'R', 'S'], [8,'T', 'U', 'V'], [9, 'W', 'X', 'Y', 'Z']]

non_fancy = ''
for fancy_n in fancy_number:
   fancy_n = fancy_n.upper()
   print ("I am trying: ", fancy_n)
   if  TODO:
      for d in db:
          if fancy_n in d:
             print (d[0])
             non_fancy = non_fancy + str(d[0])
   else:
      non_fancy = non_fancy + fancy_n

print ("The non-fancy number is: " + non_fancy)   
