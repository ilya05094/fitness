from show   import show_data
from find   import find_in
from add    import add_new_worker, add_new_ward
from delete import delete_worker,delete_ward
from error  import check_in, get_mode
from change import menu_change_info_s, menu_change_info_p
from logg   import log_start, log_quit, log_next, log_show

from global_v  import file_personal, file_clients

def comm_menu():
    print(f'\nфитнесс клуб  \n')
    return check_in(input(f'1. Сотрудники\n'
                          f'2. клиенты\n'
                           '0. Выход\n'),2)


def menu_find_personal():
    return check_in(input('\nКритерии поиска:\n'
                           '1. Фамилия\n'
                           '2. Должность\n'
                           '3. Парковочное место\n'
                           '0. Предыдущее меню\n'),3)


def menu_find_client():
    return check_in(input('\nКритерии поиска:\n'
                           '1. Фамилия\n'
                           '2. Цель тренировки\n'
                           '3. шкафчик\n'
                           '0. Предыдущее меню\n'),3)


def surname_in():
    return input('Введите фамилию: ')


def special_in():
    return input('Введите должность: ')


def parking_in():
    return input('Введите номер парковочного места: ')


def diag_in():
    return input('Введите шкафчик: ')


def locker_number_in():
    return input('Введите номер шкафчика: ')


def personal_menu():
    while check_in(input('\n1. Показать всех сотрудников\n'
                          '2. Найти сотрудника\n'
                          '3. Обновить данные сотрудника\n'
                          '4. Добавить сотрудника\n'
                          '5. Удалить данные о сотруднике\n'
                          '0. Предыдущее меню\n'),5):
        match get_mode():
            case 1:
                log_next('1')
                show_data(file_personal)
                log_show()
            case 2:
                log_next('2')
                while menu_find_personal():
                    match get_mode():
                        case 1:
                            log_next('1')
                            find_in(file_personal, 2, surname_in())
                        case 2:
                            log_next('2')
                            find_in(file_personal, 3, special_in())
                        case 3:
                            log_next('3')
                            find_in(file_personal, 5, parking_in())
            case 3:
                log_next('3')
                menu_change_info_s(file_personal)
            case 4:
                log_next('4')
                add_new_worker()
            case 5:
                log_next('5')
                delete_worker()



def client_menu():
    while check_in(input('\n1. Показать всех клиентов\n'
                          '2. Найти клиента\n'
                          '3. Обновить данные клиента\n'
                          '4. Добавить клиента\n'
                          '5. Удалить данные о клиенте\n'
                          '0. Предыдущее меню\n'),5):
        match get_mode():
            case 1:
                log_next('1')
                show_data(file_clients)
                log_show()
            case 2:
                log_next('2')
                while menu_find_client():
                    match get_mode():
                        case 1:
                            log_next('1')
                            find_in(file_clients, 1, surname_in())
                        case 2:
                            log_next('2')
                            find_in(file_clients, 2, diag_in())
                        case 3:
                            log_next('3')
                            find_in(file_clients, 3, locker_number_in())
            case 3:
                log_next('3')
                menu_change_info_p(file_clients)
            case 4:
                log_next('4')
                add_new_ward()
            case 5:
                log_next('5')
                delete_ward()


def welcome():
    log_start() 
    while comm_menu():
        match get_mode():
            case 1:
                log_next('1')
                personal_menu()
            case 2:
                log_next('2')
                client_menu()
    log_quit()