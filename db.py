# This model for writing and reading money
import csv
from decimal import Decimal


# the function to read money from file , handle the Erro, create one if not found the file
def read_money():
    try:
        with open('money.txt', 'r') as file:
            reader = csv.reader(file)
            money = next(reader)
            return Decimal(money[0])
    except FileNotFoundError:
        print("Money file not found.Creating new one")
        write_money(100)
        return 100


# write the curent amount of money to csv file
def write_money(money):
    with open('money.txt', 'w') as file:
        writer = csv.writer(file)
        writer.writerow([money])
