from customers_name_ask.customers_ask_1 import ask_name
from basic_functions.number_checker import number_checker


def box_dim(user_name):
    box_height = number_checker("Hello {}, how tall is the box you will be returning your item/s? (cm) ".format(user_name))
    box_width = number_checker("what is the width of your box? ")
    box_depth = number_checker("what is the depth of your box? ")
    box_volume = box_depth * box_height * box_width

    return box_volume
if __name__ == '__main__':
    name = ask_name()
