from logg import log_error

mode = 0

def get_mode():
    return mode

def check_in(in_mode, upper:int):
    global mode
    if not in_mode.isdigit():
       log_error('incorrect input')
       return check_in(input(f'Некорректный ввод\nВыберите пункт меню от 0 до {upper}: '), upper)
    mode = int(in_mode)
    if mode < 0 or mode not in range(0, upper+1):
       log_error('incorrect input')
       return check_in(input(f'Некорректный ввод\nВыберите пункт меню от 0 до {upper}: '), upper)
    else:
       return mode     

def exception_name(message):
    for i in "!@#$%^&/*?<>1234567890`~'\'":
        if message.find(i) > 0:
            return False
    else:
        return True


def exception_menu_item(value):
    if value.isdigit() and (int(value) in [1, 2, 3, 4, 5, 6, 7]):
        return True
    else:
        return False


def exception_id(value):
    value = value.replace(" ", '')
    if value.isdigit() and len(value) < 4:
        return True
    else:
        return False

def exception_number(value):
    if value.isdigit():
        return True
    else:
        return False



def make_choise(min: int, max: int):
    try:
        token = (int(input('Выберете операцию: ')))
    except ValueError:
        print('Это не число. Попробуйте снова')
        log_error("Incorrect input")
        return make_choise(min, max)
    if token >= min and token <= max:
        return token
    else:
        print('Попробуйте снова')
        log_error('Incorrect input')
        return make_choise(min, max)


def error_name(what: str):
    try:
        name = (input('Введите {}: '.format(what)))
    except ValueError:
        print('Это не текст. Попробуйте снова')
        log_error('Incorrect input')
        return error_name(what)
    if not name.isdigit():
        return name
    else:
        print('Вы ввели число. Попробуйте снова')
        log_error('Incorrect input')
        return error_name(what)


def error_phone(what: str):
    try:
        phone = (input(f'Введите {what}, состоящий из 11 цифр, вместе с 8-кой: '))
    except ValueError:
        print('Попробуйте снова')
        log_error('Incorrect phone entered')
        return error_phone(what)
    if phone.isdigit() and len(phone)== 11 and phone[0] == '8':
        return phone
    else:
        print('Попробуйте снова')
        log_error('Incorrect phone entered')
        return error_phone(what)


def file_name():
    try:
        token = (input('Введите название файла '))
    except ValueError:
        print('Это не текст. Попробуйте снова')
        log_error('Incorrect filename entered')
        return file_name()
    if '.txt' in token:
        return token
    else:
        print('Попробуйте снова')
        log_error('Incorrect filename entered')
        return file_name()

def size_roba(size:str):
    if size in ["XXS", "XS", "S", "M", "L", "XL", "XXL", "XXXL"]:
        return True
    else:
        return False

def void_check(size:str):
    if size not in ["", " "]:
        return True
    else:
        return False