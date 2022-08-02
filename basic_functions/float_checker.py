# asks the user the inputted question and checks if it is an float and only allows floats to be inputted
def int_checker(question):
    while True:
        try:
            number = float(input(question))
            if number < 0.00:
                print('<error> please enter a number above 0')
                print("")
            else:
                return number
        except ValueError:
            print("<error> please enter a number")
            print("")


# this is for testing the functions for errors
if __name__ == '__main__':
    num = int_checker("enter a number ")
    print(num)
