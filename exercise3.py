''' Exercise 3: 
    Print characters present at an even index number
    Write a Python code to accept a string from the user and display characters present at an even index number.
    For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.'''

def evenCharacter():
    string = input("Write something: ")
    print('Orginal String is: ', string)
    print("Printing only even index characters...")
    #Using 0 as start, rounding the lenght of 'string' and 2 for even positions
    for i in range(0, (len(string) -1), 2):
        print(string[i])

if __name__ == '__main__':
    evenCharacter()