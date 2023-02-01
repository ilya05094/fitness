import csv
def show_data(file):
    with open(file, newline='', encoding="utf8") as File:  
        reader = csv.reader(File)
        for row in reader:
            print(row)


