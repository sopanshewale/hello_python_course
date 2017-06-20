import sys

def drop_duplicates(l):
    d = {}
    for e in l:
       d[e] = 1
    return d.keys() 

my_list_str = sys.argv[1]
my_list = my_list_str.split()
print ("Your list is: {} ".format(my_list))
print ("Your new list is: {}".format(drop_duplicates(my_list)))

