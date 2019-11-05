# def main():
#     drummers = 'ZachIsWearingAHeadband'

#     for letter in drummers:
#         if letter.isupper():
#         drummers + ' '
#     print(drummers)

def maxmin():
    grades = [100,100,0,0,67,36]

    # max for the highest
    # min for the lowest

    print(max(grades))

def mode():
    count = [1, 0, 3, 0, 2, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8]
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

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

def ifin():
    friends = ['Joe', 'Kell', 'Jack', 'Church']
    # if in statements can find something in a list
    # user input = variable can be used in this assignments
    if 'joe' in friends:
        print('Joe is a friend of Kell')


# cloud collects lots of user data

# grades = (99,44,33) can't append/mutate tuples 