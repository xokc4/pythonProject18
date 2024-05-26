import warnings

warnings.filterwarnings('ignore')
import csv
import json
import random
#Первое изменение

def generate_csv_file(file_name, rows):
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for _ in range(rows):
            row = [random.randint(1, 1000) for _ in range(3)]
            writer.writerow(row)

#Второе изменение
def find_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None
    elif discriminant == 0:
        return -b / (2 * a)
    else:
        root1 = (-b + discriminant ** 0.5) / (2 * a)
        root2 = (-b - discriminant ** 0.5) / (2 * a)
        return root1, root2
#Третье изменение

def save_to_json(func):
    def wrapper(file_name):
        with open(file_name, newline='') as csvfile:
            reader = csv.reader(csvfile)
            data = []
            for row in reader:
                a, b, c = map(int, row)
                result = func(a, b, c)
                data.append({"parameters": [a, b, c], "result": result})

        with open("results.json", 'w') as f:
            json.dump(data, f, indent=4)

    return wrapper



@save_to_json
def find_roots_with_saving(a, b, c):
    return find_roots(a, b, c)


generate_csv_file("input_data.csv", 101)
find_roots("input_data.csv")

with open("results.json", 'r') as f:
    data = json.load(f)

if 100<=len(data)<=1000:
    print(True)
else:
    print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")

print(len(data)==101)