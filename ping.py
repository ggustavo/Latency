# Network Latency Tester, Author: Gustavo Moraes
# Install matplotlib, use the coomand: 
#   pip install matplotlib

import matplotlib.pyplot as plt
from datetime import datetime
import subprocess
import time
import csv

print("Testing Network ...", flush=True)
interval = 60 * 10  

f = open('result.csv', 'w', newline='')
writer = csv.writer(f)

started = True
while (started):
    #started = False
    date_now = datetime.now()
    start_time = str(date_now.strftime("(%d-%m-%Y) %H-%M-%S"))
    
    start_time_date = str(date_now.strftime("%d/%m/%Y"))
    start_time_hour = str(date_now.strftime("%H:%M:%S"))

    p = subprocess.Popen(["ping.exe","www.google.com","-n","100"], stdout = subprocess.PIPE)
    str_val = p.communicate()[0]
    #print(str_val)
    result = str(str_val).split("tempo=")
    count = 0

    pings = []
    ms = []

    for value in result[1:]:
        count = count + 1
        pings.append(count)
        #print(value.split("ms")[0])
        ms_value = int(value.split("ms")[0])
        ms.append(ms_value)
        writer.writerow([start_time_date,start_time_hour,ms_value])
        

    plt.plot(pings, ms, color='red')
    #plt.gca().set_ylim([0,1000])
    plt.xlabel('Ping')
    plt.ylabel('Latency (MS)')
    plt.title('Latency %s' % (start_time + str(datetime.now().strftime(" to %H-%M-%S") ) ))
    #plt.show()
    plt.savefig('Test %s.png' % start_time)
    plt.clf()
    print("Round Finish, sleeping now ...", flush=True)
    time.sleep(interval)

