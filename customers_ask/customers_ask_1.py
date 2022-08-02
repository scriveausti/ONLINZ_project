from basic_functions.blank_checker import blank_checker


def ask_name():
    user_name = blank_checker("what is your name? ").title().strip()
    return user_name

# format is number, island name, price multiplier
islands = [['1','north', 1],['2','south', 1.5],['3','stewart', 2]]
island_numbers = []
for i in islands:
    num, island, not_used = i
    island_numbers.append(num)

def ask_island(total_price):
    while True:
        print("which of the three big islands the product will be returned from?")
        for i in islands:
            num, island, not_used = i
            print('{}. {} Island'.format(num,island))

        customer_island = input("please enter the number on the left ").strip()

        if customer_island in island_numbers:
            break
        else:
            print('<error> please enter 1, 2 or 3')
    for i in islands:
        num, not_used, multiplier = i
        if customer_island == num:
            total_price = total_price * multiplier

def ask_other_info():
    user_lastname = blank_checker("what is your last name").title()
    user_addres = blank_checker("what is your address? ").title()
    user_phone_number = blank_checker("what is your phone number? ")


if __name__ == '__main__':
    #user_name = ask_name()
    #print('Hello {}'.format(user_name))

    user_island = ask_island(1)
    print(user_island)