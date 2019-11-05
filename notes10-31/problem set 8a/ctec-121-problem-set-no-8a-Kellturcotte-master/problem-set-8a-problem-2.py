# problem-set-8a-problem-2.py
# Your Name

'''
- Using the file rockgroups.txt, write a program that finds the total number of rock groups whose name starts with the letter T, A, and B. - Display the totals for T, A and B separetely by printing them out. 

- Be sure to strip off the line feed at the end of each line.

- Be sure to close the file.
'''


def whichGroups():
    file = open('rockgroups.txt', 'r')
    # Need If statements
    t = 0
    a = 0
    b = 0
    for name in file:
        letter = name[0][0].upper()
        if  letter == 'T':
            t = t + 1
        if letter =='A':
            a = a + 1
        if letter =='B':
            b = b + 1
    print('The amount of bands that start with a T is:', t)
    print('The amount of bands that start with a A is:', a)
    print('The amount of bands that start with a B is:', b)
whichGroups()
