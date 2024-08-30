''' Exercise 1: 
    Calculate the multiplication and sum of two numbers
    Given two integer numbers, write a Python code to return their product only if the product is equal to or lower than 1000. 
    Otherwise, return their sum.'''

def productOrSum():
    n1 = int(input('Write ur first number: '))
    n2 = int(input('Write ur second number: '))

    if((n1 * n2) > 1000):
        return f'The result is: {n1 * n2}'
    else:
        return f'The result is: {n1 + n2}'

if __name__ == '__main__':
    print(productOrSum())