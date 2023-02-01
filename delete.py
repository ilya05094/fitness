import csv
from logg import log_error
from global_v import file_personal, file_clients


def read_worker():
    with open('clients_fitness/Personal.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        for rec in reader:
            print(rec)


def delete_worker():
    with open('clients_fitness/Personal.csv', 'r', newline='\n', encoding='utf-8') as f:
        try:
            id_worker = input('Введите id сотрудника, информацию о котором хотите удалить: ')
        except ValueError:
            log_error()
        found = 0
        r = csv.reader(f, delimiter=";")
        nrec = []
        for rec in r:
            if rec[0] == id_worker:
                print('Запись удалена:', rec)
                found = 1
            else:
                nrec.append(rec)

        if found == 0:
            print('Ошибка, пожалуйста, попробуйте снова')
            f.close()
        else:
            with open('clients_fitness/Personal.csv', 'w', newline='', encoding='utf-8') as f:
                w = csv.writer(f, delimiter=';')
                w.writerows(nrec)
# read()
# delete_worker()

def read_ward():
    with open('clients_fitness/clients.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        for rec in reader:
            print(rec)


def delete_ward():
    with open('clients_fitness/clients.csv', 'r', newline='\n', encoding='utf-8') as f:
        try:
            id_ward = input('Введите id клиента, информацию о котором хотите удалить: ')
        except ValueError:
            log_error()
        found = 0
        r = csv.reader(f, delimiter=";")
        nrec = []
        for rec in r:
            if rec[0] == id_ward:
                print('Запись удалена:', rec)
                found = 1
            else:
                nrec.append(rec)

        if found == 0:
            print('Ошибка, пожалуйста, попробуйте снова')
            f.close()
        else:
            with open('clients_fitness/clients.csv', 'w', newline='', encoding='utf-8') as f:
                w = csv.writer(f, delimiter=';')
                w.writerows(nrec)
# read()
# delete_ward()