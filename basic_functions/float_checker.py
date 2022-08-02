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

if __name__ == '__main__':
    num = int_checker("enter a number ")
    print(num)
