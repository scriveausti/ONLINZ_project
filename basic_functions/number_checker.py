def number_checker(question):
    while True:
        number = float(input(question))
        if number > 0 and number.isdigit():
            return number
        elif number.isdigit():
            print('<error> please enter a number above 0')
            print("")
        else:
            print("<error> please enter a number")
            print("")


if __name__ == '__main__':
    num = number_checker("enter a number ")
    print(num)
