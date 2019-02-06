#read data from txt
with open("day1_input.txt") as f:
        data = [int(i) for i in f]

print len(data)

#find resultant frequency
print("Resultant Frequency: %d" %sum(data))

def loop_data():
#intialise frequnecy
    freq = 0
#intialise freqencies set
    freq_set = {0}
#loop through data, updating freq until repeat is reached
    while True:
        for change in data:
            freq += change
            if freq in freq_set:
                return freq
                break
            freq_set.add(freq)

print("First Frequency Reached Twice: %d" %(loop_data()))
