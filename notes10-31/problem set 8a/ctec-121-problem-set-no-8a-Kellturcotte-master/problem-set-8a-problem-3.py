# problem-set-8a-problem-2.py
# Your Name

'''
- Using the file rockgroups.txt, write a program that finds the total number of rock groups whose name contains 3 words and print out the total number.

- Display the name of each group that contains three words. Be sure to strip off the line feed at the end of each line.

- Be sure to close the file.
'''


def threeWordRockGroups():
    file = open('rockgroups.txt', 'r')
    # needs two accumulators 
    # could count spaces or split the list and take the length
    for name in file:

    # display each name 
    # if == 3 then add to total then print the line

    # rockBand = 'alice cooper'
    # number = rockBand.split()
    #print(len(number))

    # number = rockband.rstrip().cout(' ') + 1
    
threeWordRockGroups()
