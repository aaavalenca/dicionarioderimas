import csv
import os


def clean_csv(filename, my_str):
    with open(filename, 'rt') as c:
        str_arr_csv = c.readlines()
        if str(my_str) in str(str_arr_csv):
            print("True")


dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'rimas/a.csv')
clean_csv(filename, "algo")