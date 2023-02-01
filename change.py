from logg      import log_start, log_quit, log_next, log_show,  log_refresh, log_error
from refresh   import read_data, change_info_file
from error     import exception_menu_item, exception_name, exception_id, error_phone, exception_number

def get_value(message):
    while True:
        value = input(message)
        if exception_menu_item(value):
            return int(value)
        else:
            print("\n", "-"*20, "Invalid number, repeat input", "-"*20)


def get_name(message):
    while True:
        value = input(message)
        if exception_name(value):
            return value
        else:
            log_error('Incorrect name')
            print("\n", "-"*20, "Invalid name, repeat input", "-"*20)


def get_id(message):
    while True:
        value = input(message)
        if exception_id(value):
            return value
        else:
            log_error('Incorrect Id')
            print("\n", "-"*20, "Invalid id, repeat input", "-"*20)



def get_chamber(message):
    value = input(message)
    if exception_number(value):
        return value
    else:
        log_error('Incorrect value')
        print("\n", "-"*20, "Invalid value, repeat input", "-"*20)
        get_chamber(message)


def to_continee(messege):
    input(messege)


def menu_change_info_p(file_clients):
    id = get_id("Input id client: ")
    data = read_data(file_clients)
    if data[0] == 0:
        return ""
    for i in data:
        i_temp = i.replace("\n", '').split(';')
        if i_temp[0] == id:
            print(
                f"client found - {i_temp[1]} {i_temp[2]}, training goals  - {i_temp[3]}, chamber - {i_temp[4]}")
            id, last_name, first_name, training_goal, chamber, size_cp, status = i_temp
            break
    else:
        log_error('The id is missing!')
        return print("The id is missing!")
    print()
    print("1 last_name", "2 first_name", "3 training goals", "4 chamber",
          "5 size_cp", "6 status", "7 return to the previous menu",  sep="\n")
    num = get_value("\n Select item for change: ")
    log_next('id found')
    match num:
        case 1:
            last_name = get_name('Input last name: ')
            to_continee("To continue press Enter")
        case 2:
            first_name = get_name('Input first name: ')
            to_continee("To continue press Enter")
        case 3:
            training_goal = get_name('Input training goal: ')
            to_continee("To continue press Enter")
        case 4:
            chamber = get_chamber('Input chamber: ')
            to_continee("To continue press Enter")
        case 5:
            size_cp = get_name('Input size_cp: ')
            to_continee("To continue press Enter")
        case 6:
            status = get_name('Input  status: ')
            to_continee("To continue press Enter")
        case 7:
            return 0
    log_refresh()
    change_info_file(file_clients, id, last_name, first_name,
                     training_goal, chamber, size_cp, status)


def menu_change_info_s(file_personal):
    id = get_id("Input id employee: ")
    data = read_data(file_personal)
    if data[0] == 0:
        log_error('Incorrect input')
        return print('error')
    for i in data:
        i_temp = i.replace("\n", '').split(';')
        if i_temp[0] == id:
            print(
                f" employee - {i_temp[1]} {i_temp[2]}, specialization  - {i_temp[3]}, telephone - {i_temp[4]}")
            id, last_name, first_name, specialization, telephone, place, client = i_temp
            break
    else:
        log_error('The id is missing!')
        return print("The id is missing!")
    print()
    print("1 last_name", "2 first_name", "3 specialization", "4 telephone",
          "5 place", "6 client ", "7 return to the previous menu",  sep="\n")
    num = get_value("\n Select item for change: ")
    log_next('Id found - proceeding')
    match num:
        case 1:
            last_name = get_name('Input last name: ')
            to_continee("To continue press Enter")
        case 2:
            first_name = get_name('Input first name: ')
            to_continee("To continue press Enter")
        case 3:
            specialization = get_name('Input specialization: ')
            to_continee("To continue press Enter")
        case 4:
            telephone = error_phone('telephone')
            to_continee("To continue press Enter")
        case 5:
            place = get_name('Input parking place number: ')
            to_continee("To continue press Enter")
        case 6:
            client = get_name('Input  client: ')
            to_continee("To continue press Enter")
        case 7:
            # personal_menu()
            return 0
    log_refresh()
    change_info_file(file_personal, id, last_name, first_name,
                     specialization, telephone, place, client)
