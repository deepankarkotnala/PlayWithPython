import csv
import random
import time
import psutil

x_value = 0
cpu_usage = 0
ram_usage = 0

fieldnames = ["x_value", "cpu_usage", "ram_usage"]

with open('cpu_ram_data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:

    with open('cpu_ram_data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "x_value": x_value,
            "cpu_usage": psutil.cpu_percent(),
            "ram_usage": psutil.virtual_memory()[2]
        }

        csv_writer.writerow(info)
        print(('CPU:{}%'.format(info['cpu_usage'])).ljust(10),'RAM:{}%'.format(info['ram_usage']))
        x_value += 1

    time.sleep(0.2)