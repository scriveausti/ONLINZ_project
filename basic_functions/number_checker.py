def number_checker(question):
    while True:
        try:
            number = int(input(question))
            if number > 0:
                return number
            else:
                print('<error> please enter a number above 0')
                print("")
        except:
            print("<error> please enter a number")
            print("")



if __name__ == '__main__':
    num = number_checker("enter a number ")
    print(num)
