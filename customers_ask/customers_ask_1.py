def ask_name():
    while True:
        user_name = input("what is your name? ").title().strip()
        if user_name != "":
            break
        else:
            print("<error> please enter your name and don't leave it blank")
            print("")
    return user_name

def ask_island():
    while True:
        print("")
        customer_island = input("")

if __name__ == '__main__':
    user_name = ask_name()
    print('Hello {}'.format(user_name))
