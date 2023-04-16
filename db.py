# This model for writing and reading money
import csv
def read_money():
    try:
        with open('money.txt','r') as file:
            reader = csv.reader(file)
            money = next(reader)
            return float(money[0])
    except FileNotFoundError:
        print("Money file not found.Creating new one")
        write_money(100)
        return 100


def write_money(money):
    with open('money.txt','w') as file:
        writer = csv.writer(file)
        writer.writerow([money])


