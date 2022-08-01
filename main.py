from customers_ask.customers_ask_1 import ask_name,ask_island
from box.box_dimetions import box_dim
from basic_functions.welcome import welcome

if __name__ == '__main__':
    welcome()
    user_name = ask_name()
    total_price = box_dim(user_name)
    total_price =ask_island(total_price)
