import numpy as np
from datetime import datetime
import time
from collections import OrderedDict

def open_inputs():
    with open('day4_inputs.txt') as file:
        global data
        data = file.read()
open_inputs()

def process_inputs():
    global inputs
    #process inputs (clean up)
    inputs = data.replace('[1518-','').replace(']','')
    inputs = inputs.replace('wakes up','w').replace('falls asleep','s')
    inputs = inputs.replace('Guard #','').replace(' begins shift', '')

    #split inputs by line into array
    inputs = inputs[0:len(inputs)-1].split("\n")
    inputs = np.asarray(inputs)
process_inputs()

def Guard_IDs():
    #find guard IDs
    global Guard_IDs
    Guard_IDs = []
    for item in inputs:
        if not 's' in item and not 'w' in item:
            Guard_IDs.append(item[12:])

    Guard_IDs = list(set(Guard_IDs))
    Guard_IDs = [int(x) for x in Guard_IDs]
    Guard_IDs.sort()
Guard_IDs()

def num_entries():
    #calculate number of entries
    global x
    x = len(inputs)
    print('Number of notes: %d' %x)
    global rota
    rota = sorted(inputs)
num_entries()

# initialise values for sleep/wake records
records = []

def mins_between(d1, d2):
    # use to calculate sleep/wake durations
    d1 = datetime.strptime(d1, "%m-%d %H:%M")
    d2 = datetime.strptime(d2, "%m-%d %H:%M")
    # Convert to Unix timestamp
    d1_ts = time.mktime(d1.timetuple())
    d2_ts = time.mktime(d2.timetuple())
    return (d2_ts - d1_ts)/60


#def mins_range(d1, d2):
#    time_delta = mins_between(d1, d2)
#    for t in range(1,time_delta):


print(mins_between(rota[5][0:11],rota[6][0:11]))

def die():
    print("something went wrong")

def rota_end(x):
    if x == len(inputs)-1:
        return True
    else:
        return False

for x in range(0,len(inputs)):
    if not 's' in rota[x] and not 'w' in rota[x]:
        total_sleep_duration = 0
        total_wake_duration = 0
        list_row = []
        ID = rota[x][12:]
        list_row.append(int(ID))
        start_wake = rota[x][0:11]


    elif 'w' in rota[x]:
        # make this sleep_duration function
        #global start_wake
        start_wake = rota[x][0:11]
        #print("Start wake - %s" %start_wake)
        sleep_duration = int(mins_between(start_sleep, start_wake))
        #print("Sleep duration - %s" %sleep_duration)
        #global total_sleep_duration
        total_sleep_duration += sleep_duration
        if rota_end(x) == True:
            list_row.append(int(total_sleep_duration))
            list_row.append(int(total_wake_duration))
            records.append(list_row)
            break
        elif rota_end(x) == False:
            if not 's' in rota[x+1] and not 'w' in rota[x+1]:
                list_row.append(int(total_sleep_duration))
                list_row.append(int(total_wake_duration))
                records.append(list_row)

    elif 's' in rota[x]:
        # make this wake_duration function
        #global start_sleep
        start_sleep = rota[x][0:11]
        #print("Start sleep = %s" %start_sleep)
        #end_wake = rota[x][0:11]
        #print('end_wake = %s' %end_wake)
        wake_duration = int(mins_between(start_wake, start_sleep))
        #wake = mins_between(start_wake, end_wake)
        #print("Wake duration was - %s" %wake_duration)
        #global total_wake_duration
        total_wake_duration += wake_duration
        if rota_end(x) == True:
            list_row.append(int(total_sleep_duration))
            list_row.append(int(total_wake_duration))
            records.append(list_row)
            break
        elif rota_end(x) == False:
            if not 's' in rota[x+1] and not 'w' in rota[x+1]:
                list_row.append(int(total_sleep_duration))
                list_row.append(int(total_wake_duration))
                records.append(list_row)
    else:
        die()

records_array = np.array(records)
sleep_array = []

def Guards_total_sleep():
    for ID in Guard_IDs:
        sleep_sum = 0
        global indexes
        indexes = np.where(np.isin(records_array[:,0], ID))

        #print (indexes[0][0]) # prints first index value in tuple

        for i in range(0,len(indexes[0][:])):
            index = int(indexes[0][i])
            sleep = records_array[index,1]
            sleep_sum += sleep
        Guard_sleep = [ID,sleep]
        global sleep_array
        sleep_array.append(Guard_sleep)


Guards_total_sleep()
def find_max_sleep():
    global sleep_array
    sleep_array = np.array(sleep_array)
    max_sleep = (np.argmax(sleep_array[:,1]))
    global Guard_ID_max_sleep
    Guard_ID_max_sleep = sleep_array[max_sleep][0]
    print("The Guard who slept the most was: %d" %Guard_ID_max_sleep)

find_max_sleep()


#find minute Guard slept the most#
def sleep_minutes(id):
    global ID_indexes
    ID_indexes = []
    Guard_sleep_rota = []
    for x in range(0,len(inputs)):
        if id in rota[x]:
            ID_indexes.append(int(x))
    for i in ID_indexes:
        for n in range(i,999999):
            Guard_sleep_rota.append(rota[n])
            if not 's' in rota[n+1] and not 'w' in rota[n+1]:
                break
    print Guard_sleep_rota
    for s in range(0,len(Guard_sleep_rota)):
        if 's' in Guard_sleep_rota[s]:
            d1 = Guard_sleep_rota[s][0:11]
            d2 = Guard_sleep_rota[s+1][0:11]
            sleep_time = mins_between(d1, d2)
            print sleep_time
            print type(sleep_time)

sleep_minutes('%s' %Guard_ID_max_sleep)

#print(sleep_array)
#print(Guard_IDs)
#print(np.where(np.isin(records_array[:,0],'617')))
