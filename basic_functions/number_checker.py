def number_checker(question):
    while True:
        try:
            number = int(input(question))
            return number
        except:
            print("<error> please enter a number")
            print("")



if __name__ == '__main__':
    num = number_checker("enter a number ")
    print(num)
