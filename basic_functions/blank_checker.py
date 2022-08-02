def blank_checker(question):
    while True:
        thing = input(question).strip()
        if thing == "":
            print("<error> please don't leave this blank")
        else:
            break
    return thing


if __name__ == '__main__':
    blank_checker('enter something')