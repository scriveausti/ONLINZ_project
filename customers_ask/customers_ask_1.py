from basic_functions.blank_checker import blank_checker
from basic_functions.int_checker import int_checker
from basic_functions.isdigit_checker import digit_checker

# asks the user for there name and then saves it to a variable called user_name
def ask_name():
    while True:
        user_name = blank_checker("what is your name? \n").title()
        if digit_checker(user_name) == False:
            return user_name


# format is number for user to select , island name, price multiplier
islands = [['1', 'north', 1], ['2', 'south', 1.5], ['3', 'stewart', 2]]

# adds the number for user to select to a list called island_numbers
island_numbers = []
for i in islands:
    num, not_used, not_used2 = i
    island_numbers.append(num)


# asks the user for what island they will be returning the package from and then multiplies the base rate by that amount
def ask_island(total_price):
    while True:
        print("which of the three big islands the product will be returned from?")
        for i in islands:
            num, island, not_used = i
            print('{}. {} Island'.format(num, island))

        customer_island = input("please enter the number on the left ").strip()

        if customer_island in island_numbers:
            break
        else:
            print('<error> please enter 1, 2 or 3')
    for i in islands:
        num, not_used, multiplier = i
        if customer_island == num:
            total_price = total_price * float(multiplier)
            return total_price

# asks the user for their last name,
def ask_other_info(user_name, total_price):
    while True:
        user_lastname = blank_checker("what is your last name? \n").title()
        if digit_checker(user_lastname) == False:
            break
    user_address = blank_checker("what is your address? \n").title()
    user_phone_number = int_checker("what is your phone number? \n")
    user_info = [user_name, user_lastname, user_address, user_phone_number, total_price]
    return user_info

# this is for testing the functions for errors
if __name__ == '__main__':
    while True:
        user_name = ask_other_info('Austin', 9.00)
        print('accepted, input: {}'.format(user_name))

