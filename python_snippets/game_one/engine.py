import random


def think_num():
    global num
    num = random.sample('1234567890', 4)
    if num[0] == 0:
        random.shuffle(num)
    return num
def check_num(user_num):
    global bulls_cows
    bulls_cows = {'bulls': 0, 'cows': 0}
    for number, i in enumerate(num):
        if user_num[number]==i:
            bulls_cows['bulls']+=1
        elif user_num[number] in num:
            bulls_cows['cows']+=1
    print(bulls_cows)
def compare(value_num):
    if list(value_num)==num:
        return 1

