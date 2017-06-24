import re
import matplotlib.pyplot as plt 

year = []
finish_time=[]

with open("100_meter.csv", 'r') as f:
    for line in f:
        line = re.sub(r'\s+', '', line)
        records = line.split(',')
        #print(records)
        if records[0] != '' and records[0]!='Year':
            year.append(int(records[0]))
            finish_time.append(float(records[1]))
#print(year)
#print (finish_time)
plt.bar(year, finish_time)
plt.xlabel('Year')
plt.ylabel('Time')
plt.show()
