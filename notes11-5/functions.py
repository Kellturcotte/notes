# fill in the () of a function with a variable that variable recives any data from other functions and is assgined that value 
def hsu(p,q): # p = string (can use list & int), q = number
    print(p)

def ryek():
    print('Yes Sir')
    

# varibles are stck in functions unless the function is called
def main():
    pizza = 'Rally'
    # sends the value of the varible pizza to hsu 
    hsu(pizza,42)
    # arguement^ [arguements can send base values instead of just variables]
    

    # # use range to call function multiple times
    # for i in range(100):
    #     ryek()

main()

# # a function can give information after the function
# x = main()

# print(x)