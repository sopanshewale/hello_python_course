number = int(input("How many records you would like to enter in PhoneBook? "))
print ("Please enter those required (One record on each line, they should be space seperated).")

phone_book = {}
while 0<number:
    record = input()
    records = record.split()
    phone_book[records[0]] = records[1] 
    number = number - 1

print ('''Your records are entered in phonebook successfully. Now, please enter names which you would like to query? 
(Once done - feel free to enter ctrl+D)''')

queries = []
try: 
   while True: 
           s = input()
           queries.append(s)
except EOFError: 
    pass

print ("Printing Phone Numbers for queries names:")

for e in  queries:
   if e in phone_book:
        print ("{} = {}".format(e, phone_book[e]))
   else: 
       print("For {} - Number not found".format(e))


