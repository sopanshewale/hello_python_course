import sys
d = {'Jan':1, 'Feb':2, 'Mar':3, 'Dec': 12}
my_d = sys.argv[1]
fields = my_d.split()
try: 
   print ("{}/{}/{}".format(d[fields[1]], fields[0] , fields [2] ))
except: 
  print ("ERROR: something went wrong")
