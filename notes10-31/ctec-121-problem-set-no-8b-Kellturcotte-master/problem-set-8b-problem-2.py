# problem-set-8b-problem-2.py
# Kell Turcotte

'''
Word Separator

Write a program that accepts as input a sentence in wich all of the words are run together but the first character of each word is in upper case. Convert the sentence to a new string in which the words are separted by spaces and ONLY THE FIRST WORD OF THE SENTENCE is an uppercase letter.

For example, the string "ILikePizza" should be converted to "I like pizza".

A second example "BruceGivesTonsOfAssignments" should be converted to "Bruce gives tons of assignments"

I have provided some starter code to help you get started.
'''


def main():
    # initialize variable
    result = ''

    # Receive user input.
    user_string = input('Enter a string: ').title()

    # Copy first letter in the string in its capitalized form.
    result = result + user_string[0]

    for i in range(1, len(user_string)):  # note loop starts at 1
        # get character
        ch = user_string[i]
        # If the next character is in upper case set a space
        # for the new word and convert the letter to lower case.
        # use the .isupper() string method and a decision structure
        if ch.isupper():
            ch += ' '
        result = ch + result
        # other logic goes here as well

    result.sort(reverse=Ture)
    print(result)


# Call the main function.
main()
