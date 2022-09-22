

def digit_checker(answ):
    if not answ.isdigit():
        return False
    else:
        print("<error> please don't just enter digits\n")
        return True
