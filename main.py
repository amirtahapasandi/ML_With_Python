# text = "Cyres the great"

# print(f"{text}")
# print(f"{text:#<20}")
# print(f"{text:_>20}")
# print(f"{text:.^20}")
import csv

with open("csv_file") as data_csv_file:
    data_reader_csv_file = csv.reader(data_csv_file)