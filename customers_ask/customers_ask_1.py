def ask_name():
    while True:
        user_name = input("what is your name? ").title().strip()
        if user_name != "":
            break
        else:
            print("<error> please enter your name and don't leave it blank")
            print("")
    return user_name


islands = ['1','2','3']

def ask_island(total_price):
    while True:
        print("""what island are you in 
        1. North Island 
        2. South Island
        3. Stewart Island""")
        customer_island = input("please enter the number on the left ")
        if customer_island in islands:
            break
        else:
            print('<error> please enter 1, 2 or 3')
    if customer_island == '2':
        total_price = total_price * 1.5
    elif customer_island == '3':
        total_price = total_price * 2
    return total_price

if __name__ == '__main__':
    user_name = ask_name()
    print('Hello {}'.format(user_name))
