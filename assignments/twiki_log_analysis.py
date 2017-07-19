topics = {}
with open ("tmp_twiki_sized.log", 'r') as f:
   for line in f:
        tmp_list = line.split('| ')
        print (tmp_list) 

