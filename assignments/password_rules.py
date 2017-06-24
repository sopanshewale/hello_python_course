import sys
password  = sys.argv[1]

#debug
print ("Your password is: {}".format(password))

x = True 
while x:
      if len(password) > 6 or  len(password)<20 or re.search('[a-z]', password): 
          break
      else:
          print (password, ' is valid')
          x = False


if x:
   print (password, 'is not valid')

