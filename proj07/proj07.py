import csv
import copy
from typing import List, Dict, Tuple, TextIO, Union
from datetime import datetime
from operator import itemgetter

COLUMNS = ["date",  "average temp", "high temp", "low temp", "precipitation", \
            "snow", "snow depth"]
TOL = 0.02
BANNER = 'This program will take in csv files with weather data and compare \
the sets.\nThe data is available for high, low, and average temperatures,\
\nprecipitation, and snow and snow depth.'    
MENU = '''
        Menu Options:
        1. Highest value for a specific column for all cities
        2. Lowest value for a specific column for all cities
        3. Average value for a specific column for all cities
        4. Modes for a specific column for all cities
        5. Summary Statistics for a specific column for a specific city
        6. High and low averages for each category across all data
        7. Quit
        Menu Choice: '''


def open_files() -> Union[List[str], List[TextIO]]:
    ''' Docstring'''
    while True:
        cities = []
        cities_fp = []
        str_list = input("Enter cities names: ")
        str_list = str_list.strip()
        str_list = str_list.split(",")
        for city in str_list:
            try:
                city = city.strip()
                city_fp = open(city + ".csv", "rt")
                cities.append(city)
                cities_fp.append(city_fp)
            except FileNotFoundError:
                print(f"Error: File {city}.csv is not found")
                break
        if len(cities) == len(str_list):
            return cities, cities_fp


def null_float(value: str) -> float:
    ''' Docstring'''
    if value == "":
        return None
    else:
        return float(value)


def read_files(cities_fp: List[TextIO]) -> List[List[Tuple[str, float, float, float, float, float, float]]]:
    ''' Docstring'''
    output = []
    for fp in cities_fp:
        data = []
        reader = csv.reader(fp)
        next(reader)
        next(reader)
        for row in reader:
            date = row[0]
            average_temp = null_float(row[1])
            high_temp = null_float(row[2])
            low_temp = null_float(row[3])
            precipitation = null_float(row[4])
            snow = null_float(row[5])
            snow_depth = null_float(row[6])
            data.append((date, average_temp, high_temp, low_temp, precipitation, snow, snow_depth))
        output.append(data)
    return output


def get_data_in_range(master_list: List[List[Tuple[str, float, float, float, float, float, float]]], start_str: str, end_str: str) -> List[List[Tuple[str, float, float, float, float, float, float]]]:
    ''' Docstring'''
    start_date = datetime.strptime(start_str, "%m/%d/%Y").date()
    end_date = datetime.strptime(end_str, "%m/%d/%Y").date()
    new_master_list = copy.deepcopy(master_list)
    for city in new_master_list:
        for row in city:
            date = datetime.strptime(row[0], "%m/%d/%Y").date()
            if date < start_date or date > end_date:
                city.remove(row)
    return new_master_list


def get_min(col: int, data: List[List[Tuple[str, float, float, float, float, float, float]]], cities: List[str]) -> Tuple[str, float]:
    ''' Docstring'''
    min_values = []
    for city in data:
        city_row = []
        for row in city:
            if row[col] != None:
                city_row.append(row[col])
        min_values.append(min(city_row))
    output = []
    for city in cities:
        output.append((city, min_values[cities.index(city)]))
    return output   # remove this line


def get_max(col: int, data: List[List[Tuple[str, float, float, float, float, float, float]]], cities: List[str]) -> Tuple[str, float]: 
    ''' Docstring'''
    max_values = []
    for city in data:
        city_row = []
        for row in city:
            if row[col] != None:
                city_row.append(row[col])
        max_values.append(max(city_row))
    output = []
    for city in cities:
        output.append((city, max_values[cities.index(city)]))
    return output   # remove this line


def average(lst): 
    return sum(lst) / len(lst)


def tol_eq(a, b):
    return abs((a - b) / a) < TOL


def remove_duplicates(lst):
    output = []
    for i in lst:
        if i not in output:
            output.append(i)
    return output


def multi_max(lst):
    output = []
    max(lst, key=itemgetter(1))[1]
    for i in lst:
        if i[1] == max(lst, key=itemgetter(1))[1]:
            output.append(i[0])
    return output


def mode(lst):
    lst = sorted(lst)
    counts = []
    streak_num = lst[0]
    streak_count = 1
    for i in range(1, len(lst)):
        if tol_eq(lst[i], streak_num):
            streak_count += 1
        else:
            counts.append((streak_num, streak_count))
            streak_num = lst[i]
            streak_count = 1
        counts.append((streak_num, streak_count))
        counts = list(set((counts)))
    return multi_max(counts), max(counts, key=itemgetter(1))[1]


def get_average(col: int, data: List[List[Tuple[str, float, float, float, float, float, float]]], cities: List[str]) -> Tuple[str, float]: 
    ''' Docstring'''
    avg_values = []
    for city in data:
        city_row = []
        for row in city:
            if row[col] != None:
                city_row.append(row[col])
        avg_values.append(average(city_row))
    output = []
    for city in cities:
        output.append((city, round(avg_values[cities.index(city)], 2)))
    return output


def get_modes(col: int, data: List[List[Tuple[str, float, float, float, float, float, float]]], cities: List[str]) -> Tuple[str, float]:
    ''' Docstring'''
    mode_values = []
    for city in data:
        city_row = []
        for row in city:
            if row[col] != None:
                city_row.append(row[col])
        mode_values.append(mode(city_row))
    output = []
    for city in cities:
        if mode_values[cities.index(city)][1] == 1:
            output.append((city, [], mode_values[cities.index(city)][1]))
        else:
            output.append((city, mode_values[cities.index(city)][0], mode_values[cities.index(city)][1]))
    return output


def high_low_averages(data, cities, categories):
    ''' Docstring'''
    output = []
    for category in categories:
        try:
            col = COLUMNS.index(category)
            averages = get_average(col, data, cities)
            averages = sorted(averages, key=itemgetter(0))
            averages = sorted(averages, key=itemgetter(1))
            output.append([(averages[0][0], averages[0][1]), (averages[-1][0], averages[-1][1])])
        except ValueError:
            output.append(None)
    return output 


def display_statistics(col, data, cities):
    ''' Docstring'''
    averages = get_average(col, data, cities)
    modes = get_modes(col, data, cities)
    mins = get_min(col, data, cities)
    maxs = get_max(col, data, cities)
    modes_str = ""
    for i in modes:
        modes_str = modes_str.join(f"{i[1][0]},")
    modes_str = modes_str[:-1]
    for i in range(len(cities)):
        print(f"{cities[i]}:")
        print(f"Min: {mins[i][1]:.2f} Max: {maxs[i][1]:.2f} Avg: {averages[i][1]:.2f}")
        print(f"Most common repeated values ({modes[0][2]} occurrences): {modes_str}")
    pass   # remove this line


def main():
    cities, fps = open_files()
    master_list = read_files(fps)
    display_statistics(3, master_list, cities)
    pass

if __name__ == "__main__":
    main()
