# asks the user the inputted question and checks if it is an integer and only allows integers to be inputted
def int_checker(question):
    while True:
        try:
            number = int(input(question))
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
    while True:
        num = int_checker("enter a number ")
        print("input accepted : {}".format(num))
