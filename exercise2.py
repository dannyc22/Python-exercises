''' Exercise 2:
    Print the Sum of a Current Number and a Previous number
    Write a Python code to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.'''

def totalSum():
    num = int(input('Write the range for the sum of the numbers: '))
    pre_num = 0
    for i in range (num): 
        print(f'Current Number {i} Previous Number  {pre_num}  Sum:  {i + pre_num}')
        pre_num = i



if __name__ == '__main__':
    totalSum()