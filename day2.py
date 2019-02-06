'''
a) From list of box IDs (i.e. 'abcdef'):
- Count the number that have an ID containing exactly two of any letter
- Separately count those with exactly three of any letter. 
- Multiply those two counts together to get a rudimentary checksum.

b) 
- Find the boxes with IDs which differ by exactly one character at the same position in both strings.
- Return the letters are common between the two correct box IDs.
'''

import numpy as np
import collections

def getASII():

    f = open("day2_input.txt","r")

    data = f.read()
    num_data = map(ord,data)
    global codes
    codes = [num_data[x:x+26] for x in xrange(0, len(num_data), 27)]
    #each code is 26 characters long


def doubles():
    x = len(codes) #len(codes) = 250, remember final number is not included in
                    #range(0,x)
    #initialise variables for count of doubles, triples and quadruples
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


    print("\nThere are %d doubles overall" %n_2)
    print("There are %d triples overall" %n_3)
    print("There are %d quadruples overall\n" %n_4)

def checksum():
    checksum = (n_2 * n_3 * n_4)
    print("\nChecksum = %d\n" %checksum)
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
    codes_array = np.asarray(codes) #length = 250

    for n in range(0,len(codes_array)):
        for m in range(0,len(codes_array)):
            #calculate difference in code ASCII values
            sub = np.subtract(codes_array[n],codes_array[m])
            #square each value and sum, to avoid coincidental total difference
            #of 1
            check = sum(sub**2)
            if check == 1:
                global code1
                code1 = codes_array[n]
                global code2
                code2 = codes_array[m]
                first_code = ''.join(chr(i) for i in codes_array[n])
                second_code = ''.join(chr(i) for i in codes_array[m])
                return first_code, second_code

#find list of same letters in 2 codes identified as almost identical
def same_letters():
    diff = np.subtract(code1,code2)
    indexes = np.where(diff==0)
    letters = ''.join(chr(i) for i in code1[indexes])
    return letters

print('The two box IDs which vary by one letter:\n%s \n%s' %vari_check())
print('\nLetters in common are:\n%s' %same_letters())
