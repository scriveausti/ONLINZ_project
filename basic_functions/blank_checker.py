# asks the user the inputted question and checks if it is blank if it is it says to in put the right thing
def blank_checker(question):
    while True:
        thing = input(question).strip()
        if thing == "":
            print("<error> please don't leave this blank\n")
        else:
            break
    return thing


# this is for testing the functions for errors
if __name__ == '__main__':
    while True:
        output = blank_checker('enter something')
        print("input accepted : {}".format(output))
