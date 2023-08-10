import os
import math
import re
from pathlib import Path
import time
import datetime

directory_dict = {}

def runtime_decorator(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time =time.time()
        overall_runtime = end_time - start_time
        print(f'Time taken: {math.ceil(overall_runtime)}')
        return result
    return wrapper

@runtime_decorator
def serial_number_finder(directory_path):
    entries = os.listdir(directory_path)
    for entry in entries:
        entry_path = os.path.join(directory_path, entry)
        if os.path.isdir(entry_path):
            serial_number_finder(entry_path)
        elif entry.endswith('.txt'):
            file = open(entry_path, 'r')
            data = file.read().rstrip()
            search = re.findall(r'[N][a-zA-Z]{3}-\d{5}', data)
            map_lists_to_dict(search, entry)
    print_dict()

def map_lists_to_dict(search, entry):
    directory_dict[entry] = search

def print_dict():
    print('-----------------------------------------------')
    print(f'Search Date: {datetime.datetime.now()}')
    print('File                 Serial No.')
    print('----                 ----------')
    count = 0
    for file, list in directory_dict.items():
        if file is not None:
            for serial in list:
                count +=1
                print(f'{file}              {serial}')
    print(f'Numbers found: {count}')



serial_number_finder('C:\PersonalProjects\Program-A-Day\Day_9_Serial_Number_Finder\Project+Day+9\My_Big_Directory')
