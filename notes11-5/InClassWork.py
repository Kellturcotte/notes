def product(a,b,c,d):
    return a * b * c * d

def summer(a,b,c,d):
    return a + b + c + d

def substractor(a,b,c,d):
    return a - b - c - d

def main():
    a = int(input('Enter a number: '))
    b = int(input('Enter a number: '))
    c = int(input('Enter a number: '))
    d = int(input('Enter a number: '))

    product(a,b,c,d)
    summer(a,b,c,d)
    substractor(a,b,c,d)

    print('the product is', product(a,b,c,d))
    print('the sum is', summer(a,b,c,d))
    print('the difference is', substractor(a,b,c,d))

main() 