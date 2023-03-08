from engine import think_num, check_num, compare
from colorama import Fore

user = 1
rec_list = []
step = 0
think_num()
while True:
    value_num = input((Fore.BLUE + 'Введите ваш вариант с неповторяющимися цифрами'))
    if compare(value_num):
        print(Fore.BLUE + 'победа')
        print(Fore.GREEN + 'Раунд', step)
        choice = input(Fore.YELLOW + 'Хотите еще партию?')
        if choice == 'Yes' or choice == 'yes':
            think_num()
            continue
        else:
            break
    else:
        for i in value_num:
            rec_list.append(i)
        rec_list_set = set(rec_list)
        if len(rec_list_set) == 4:
            check_num(user_num=value_num)
        else:
            print(Fore.RED + 'Вы ввели повторяющиеся цифры в номере')
        rec_list = []
        del rec_list_set
        step += 1
