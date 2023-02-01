from logg import log_find
def find_in(file: str, r: int, value: str) -> list:
    """
    Поиск по файлу данных
    требуется указать путь/имя файла, столбец в котором ищем и собственно что ищем
    просто печатает строки содержащие найденое
    возвращает список списков )
    """
    data = []
    res = []
    with open(file, newline='', encoding="utf-8") as o_file:
        reader1 = o_file.readline().replace('\ufeff', '').replace('\r\n', '')   
        reader2 = o_file.readlines()
        print(reader1)
        count = 0            
        for row in reader2:
            row = row.replace('\r\n', '')
            if row:
                res = row.split(';')
               
                if value.lower() in res[r].lower():
                    
                    print(row)
                    count += 1
                    data.append(row)
                else:
                    continue
            else:
                continue
        if not count:       
            print('По запросу ничего не найдено!')
        log_find()
        
    return data


def find_last_id(file: str) -> int:
   
    with open(file, newline='', encoding="utf-8") as o_file:
        reader1 = o_file.readline()
        reader2 = o_file.readlines()
        res = []
        data = []
        for row in reader2:
            row = row.replace('\r\n', '')
            if row:
                res = row.split(';')
                data.append(int(res[0]))
            else:
                continue
        log_find()
    return max(data)


