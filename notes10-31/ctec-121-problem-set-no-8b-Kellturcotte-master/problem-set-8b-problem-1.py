# problem-set-8b-problem-1.py
# Your Name

'''
Most Frequent Letter in a Text String

Write a Python program that lets a person enter a string and displays the character that appears the most frequently in the string.

I have provided some starter code to help you get started.
'''


def mostFrequent():
    # initial variables
    count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sentence = input('Enter a string to be analyzed: ').upper()

    for letter in sentence:
        position = letters.find(letter)
        # if value not found .find puts it as -1
        if position != -1:
            count[position] += 1
    greatest = 0
    position = 0
    greatestP = 0
    for thing in count: # iterate through string
        if thing > greatest: # compare current to the greatest thing
            greatest = thing # thing becomes new greatest
            greatestP = position # stores the position 
        position = position + 1 # increments next position
    # don't worry about mulit high points for problem set 8b problem 1
    print(letters[greatestP])

    print(count)

    # your code goes here


mostFrequent()
