import csv

path: str = "exemplo.csv"

file_csv: list = []

with open(path, mode="r", encoding="utf-8") as file:
    read_csv = csv.DictReader(file)

    for raw in read_csv:
        file_csv.append(raw)

print(file_csv)