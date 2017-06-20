import sys

def drop_duplicates(l):
    new_l = [] 
    for e in l:
        if e in new_l:
           pass 
        else:
            new_l.append(e)
    return new_l

my_list_str = sys.argv[1]
my_list = my_list_str.split()
print ("Your list is: {} ".format(my_list))
print ("Your new list is: {}".format(drop_duplicates(my_list)))

