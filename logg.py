from datetime import datetime
from global_v  import file_logs

def log_error(str: str):
    time_calc = datetime.now().strftime('%D - %H:%M:%S')
    with open(file_logs, 'a') as log_file:
        log_file.write(f'Enter error at {time_calc} - {str} \n')


def log_start():
    time_calc = datetime.now().strftime('%D - %H:%M:%S')
    with open(file_logs, 'a') as log_file:
        log_file.write(f'Start work with app at {time_calc}\n')

def log_quit():
    time_calc = datetime.now().strftime('%D - %H:%M:%S')
    with open(file_logs, 'a') as log_file:
        log_file.write(f'End of work with app at {time_calc}\n')

def log_next(str: str):
    time_calc = datetime.now().strftime('%D - %H:%M:%S')
    with open(file_logs, 'a') as log_file:
        log_file.write(f'User make new choice at {time_calc} - {str}\n')

def log_show():
    time_calc = datetime.now().strftime('%D - %H:%M:%S')
    with open(file_logs, 'a') as log_file:
        log_file.write(f'User check data at {time_calc}\n')

def log_fill():
    time_calc = datetime.now().strftime('%D - %H:%M:%S')
    with open(file_logs, 'a') as log_file:
        log_file.write(f'User add data at {time_calc}\n')

def log_find():
    time_calc = datetime.now().strftime('%D - %H:%M:%S')
    with open(file_logs, 'a') as log_file:
        log_file.write(f'User find wanted person at {time_calc}\n')

def log_refresh():
    time_calc = datetime.now().strftime('%D - %H:%M:%S')
    with open(file_logs, 'a') as log_file:
        log_file.write(f'User refreshed data at {time_calc}\n')

def log_delete():
    time_calc = datetime.now().strftime('%D - %H:%M:%S')
    with open(file_logs, 'a') as log_file:
        log_file.write(f'User delete person data at {time_calc}\n')

def log_add(fail: str, id: int):
    time_calc = datetime.now().strftime('%D - %H:%M:%S')
    with open(file_logs, 'a') as log_file:
        log_file.write(f'User add person data {time_calc} at {fail} id {id}\n')