# problem-set-8a-problem-4.py
# Your Name

'''
- Using the file rockgroups.txt, write a program that reads each rockgroup into a list. Be sure to strip off the line feed at the end of each line.

- Once you have read each line into the list, sort the list in descending order.

- Print out the list and number each lines starting at 1. Number them like 1) , 2) , 3) etc.

- Create a new file named rockgroups_sorted.txt using Python code and write out the list of sorted in descending order rockgroups.

- Be sure to close the files.
'''


def threeWordRockGroups():
    file = open('rockgroups.txt', 'r')
    i = 1
    for group in file:
        print(f'{i}) {group}')
        i += 1
    # needs .sort(reverse=Ture)
    # needs blank list  names []
    # print list with 1) to each number


threeWordRockGroups()
