from find import find_last_id
from logg import log_add
from error import exception_name, error_phone, size_roba, void_check
import csv


def add_line(lis, fail):
    with open(fail, 'a', newline='', encoding="utf-8") as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';',
                                quotechar=';', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(lis)
    log_add(fail,lis[0])


def add_new_worker():
    file = "locker number/client.csv"
    new_worker_profil = []
    new_worker_profil = add_id(new_worker_profil, file)
    new_worker_profil = add_name(new_worker_profil, 1)
    new_worker_profil = add_last_name(new_worker_profil, 1)
    new_worker_profil = add_post(new_worker_profil)
    new_worker_profil = add_phone(new_worker_profil)
    new_worker_profil = add_parking_nam(new_worker_profil)
    new_worker_profil = add_ward_id(new_worker_profil)
    add_line(new_worker_profil, file)


def add_new_ward():
    file = "locker number/client.csv"
    new_ward_profil = []
    new_ward_profil = add_id(new_ward_profil, file)
    new_ward_profil = add_name(new_ward_profil, 0)
    new_ward_profil = add_last_name(new_ward_profil, 0)
    new_ward_profil = add_training_goals(new_ward_profil)
    new_ward_profil = add_locker_number(new_ward_profil)
    new_ward_profil = add_size(new_ward_profil)
    new_ward_profil = add_status(new_ward_profil)
    add_line(new_ward_profil, file)


def add_id(lis, file):
    lis.append(find_last_id(file)+1)
    return lis


def add_name(lis, typ):
    if typ == 1:
        typ = "сотрудника"
    else:
        typ = "клиент"
    lis.append(input(f"Введите имя нового {typ}: ").strip().capitalize())
    while not exception_name(lis[1])or not void_check(lis[1]):
        lis[1]= input(f"В имени нового {typ} недопустимые символы.\nПопробуйте снова: ").strip().capitalize()
    return lis


def add_last_name(lis, typ):
    if typ == 1:
        typ = "сотрудника"
    else:
        typ = "клиента"
    lis.append(input(f"Введите фамилию нового {typ}: ").strip().capitalize())
    while not exception_name(lis[2]) or not void_check(lis[2]):
        lis[2]= input(f"В фамилии нового {typ} недопустимые символы. \nПопробуйте снова: ").strip().capitalize()
    return lis



def add_post(lis):
    lis.append(input(f"{lis[2]} {lis[1]} в должности: ").strip().capitalize())
    while not void_check(lis[3]):
        lis[3]= input(f"Нельзя оставить пустым. \nПопробуйте снова: ").strip().capitalize()
    return lis


def add_phone(lis):
    lis.append(error_phone("номер телефона")) 
    return lis


def add_parking_nam(lis):
    lis.append(input(f"{lis[3]} {lis[2]} паркуется на месте №: "))
    while not void_check(lis[5]):
        lis[5]= input(f"Нельзя оставить пустым. В случаи отсутствия ставь 0 \nПопробуйте снова: ").strip().capitalize()
    return lis


def add_ward_id(lis):
    lis.append(input(f"{lis[3]} {lis[2]} работает с клиентом id(если есть): "))
    return lis


def add_training_goals(lis):
    lis.append(input(f"Опишите цель тренировки: ").strip().capitalize())
    while not void_check(lis[3]):
        lis[3]= input(f"Нельзя оставить пустым. \nПопробуйте снова: ").strip().capitalize()
    return lis


def add_locker_number(lis):
    lis.append(input(f"Номер шкафчика: "))
    while not void_check(lis[4]):
        lis[4]= input(f"Нельзя оставить пустым. \nПопробуйте снова: ").strip().capitalize()
    return lis


def add_size(lis):
    lis.append(input(f"Размер экипировки: ").upper())
    
    while not size_roba(lis[5]) or not void_check(lis[5]) :
        lis[5]= input(f"Недопустимый размер, доступные размеры: XXS, XS, S, M, L, XL, XXL, XXXL\nПопробуйте снова:".upper())
    
    return lis


def add_status(lis):
    lis.append(input(f"Состояние (статус): ").strip().capitalize())
    while not void_check(lis[6]):
        lis[6]= input(f"Нельзя оставить пустым. \nПопробуйте снова: ").strip().capitalize()
    return lis


# lower(): переводит строку в нижний регистр
# capitalize(): переводит в верхний регистр первую букву только самого первого слова строки
