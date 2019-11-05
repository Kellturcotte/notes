# problem-set-8a-problem-1.py
# Your Name

'''
- Using the file rockgroups.txt, write a program that asks the user to enter the name of a file, in this case rockgroups.txt, and then open that file and display each line preceeded by a line number following b a colon and then a space.

- The line numbering should start at 1. 

- Be sure to strip off the line feed at the end of each line.

- Be sure to close the file.
'''


def showRockGroups():
    # Enters file name and saves as varible
    file = input('Enter file name: ')
    open(file)

showRockGroups()
