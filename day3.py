import numpy as np

# read data from file
with open("day3_input.txt", "r") as file:
    data = file.read()

#remove unwanted symbols
inputs = data.translate(None, '#:')
inputs = inputs.replace('x',' ').replace(',',' ').replace('@ ','').replace('\n',' ')

#unroll values into array of integers
inputs = inputs[0:len(inputs)-1].split(" ")
inputs = [int(i) for i in inputs]
inputs = np.asarray(inputs)
print(len(inputs))
print(type(inputs))

#calculate number of submissions
x = len(data.split("\n"))
print('Number of submissions: %d' %x)

#create template "patch" of total fabric
p = (1000,1000) # length
patch = np.zeros(p)

#for every input, calculate full list of coordinates,
#first find range of x and y for each submission
for n in range(0,len(inputs)/5):
    x_start = (inputs[(n*5+1)])
    x_end = x_start + (inputs[(n*5+3)])
    y_start = (inputs[(n*5+2)])
    y_end = y_start + (inputs[(n*5+4)])

    x_range = range(x_start, x_end)
    y_range = range(y_start, y_end)

#then for each x and y, add 1 to patches template
    for y in y_range:
        for x in x_range:
            patch[x,y] +=1

#test patch
print(patch[222:232,280:299])

#calculate number of patches with >=2
overlaps = np.count_nonzero(patch>=2)
print('There are %d inches in more than 2 different submissions\n' %overlaps)

#run loop again but this time add up values of "patch" and divide by num_points
#to get patch average
unique_patches = []
for n in range(0,len(inputs)/5):
    x_start = (inputs[(n*5+1)])
    x_end = x_start + (inputs[(n*5+3)])
    y_start = (inputs[(n*5+2)])
    y_end = y_start + (inputs[(n*5+4)])

    x_range = range(x_start, x_end)
    y_range = range(y_start, y_end)

    check = 0
#create list of unrolled coordinates
    for y in y_range:
        for x in x_range:
            check += patch[x,y]
    num_points = (len(y_range))*(len(x_range))
    if (check/num_points) == 1:
        unique_patches.append(n+1)
print('Unique patches identified: %s' %(unique_patches))

#try plotting the data
#things we need =
#plot of patches values as coordinates

import matplotlib.pyplot as plt
#plt.plot(patch)
#plt.show()

plt.imshow(patch)
plt.show()
plt.imshow(patch, interpolation='nearest')
plt.show()
