from customers_ask.customers_ask_1 import ask_name
from basic_functions.number_checker import number_checker


def box_dim(user_name):
    box_height = number_checker("Hello {}, how tall is the box you will be returning your item/s? (cm) ".format(user_name))
    box_width = number_checker("what is the width of your box? (cm) ")
    box_depth = number_checker("what is the depth of your box? (cm) ")
    box_volume = box_depth * box_height * box_width
    if box_volume <= 6000:
        price = 8.00
    elif 6000 < box_volume < 100000:
        price = 12.00
    else:
        price = 15.00
    return price


if __name__ == '__main__':
    name = ask_name()
    total_price = box_dim(name)
    print(total_price)