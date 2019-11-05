stuff = "HiThereGuys"

for letter in stuff:
    if letter.isupper():
        print(letter, 'is upper')

def index():
    grades = [0,0,3,0,0,0]
    letters = 'ABCDEF'
    biggest = max(grades)
    print(biggest)
    position = grades.index(biggest)
    # index finds the position in letters
    print(letters[position])