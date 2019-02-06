import numpy as np
import collections

def getASII():

    f = open("day2_input.txt","r")

    data = f.read()
    num_data = map(ord,data)
    global codes
    codes = [num_data[x:x+27] for x in xrange(0, len(num_data), 27)]
    #spaces were included at the end of each string, therefore each must be 27 long


def doubles():
    x = len(codes) #len(codes) = 250, remember final number is not included in
                    #range(0,x)
    global n_2
    global n_3
    global n_4
    n_2 = 0
    n_3 = 0
    n_4 = 0

    for r in range(0,x):
        doubles = len([item for item, count in collections.Counter(codes[r]).items() if 3 > count > 1])
        if doubles >= 1:
            n_2 += 1
        triples = len([item for item, count in collections.Counter(codes[r]).items() if 4 > count > 2])
        if triples >= 1:
            n_3 += 1
        quads = len([item for item, count in collections.Counter(codes[r]).items() if 5 > count > 3])
        if quads >= 1:
            n_4 += 1


    print("There are %d doubles overall" %n_2)
    print("There are %d triples overall" %n_3)
    print("There are %d quadruples overall" %n_4)

def checksum():
    checksum = (n_2 * n_3 * n_4)
    print("Checksum = %d" %checksum)
getASII()
doubles()

#make sure no 0 to ruin checksum
if n_2 == 0:
    n_2 += 1
if n_3 == 0:
    n_3 += 1
if n_4 == 0:
    n_4 += 1

checksum()

def vari_check():
    codes_array = np.asarray(codes)
    for n in range(0,len(codes_array)):
        for m in range(0,len(codes_array)):
            sub = np.subtract(codes_array[n],codes_array[m])
            check = sum(sub**2)
            if check == 1:
                global code1
                code1 = codes_array[n]
                global code2
                code2 = codes_array[m]
                first_code = ''.join(chr(i) for i in codes_array[n])
                second_code = ''.join(chr(i) for i in codes_array[m])
                return first_code, second_code

def same_letters():
    diff = np.subtract(code1,code2)
    indexes = np.where(diff==0)
    letters = ''.join(chr(i) for i in code1[indexes])
    return letters

print(vari_check())
print(same_letters())
