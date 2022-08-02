from customers_ask.customers_ask_1 import ask_name, ask_island, ask_other_info
from box.box_dimetions import box_dim
from basic_functions.welcome import welcome

if __name__ == '__main__':
    welcome()
    user_name = ask_name()
    total_price = box_dim(user_name)
    total_price = ask_island(total_price)
    user_info = ask_other_info(user_name,total_price)
    print("user's name : {} {}, user's address : {}, user's phone number : {}, total returning price : ${}".format(user_info[0],user_info[1],user_info[2],user_info[3],user_info[4]))