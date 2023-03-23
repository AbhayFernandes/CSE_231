###########################################################
#  Computer Project #7
#
#  Algorithm
#    1.  Print a welcome message
#    2.  Prompt the user for a file name
#    3.  Show the menu, ask for a choice
#    4.  Based on their choice, do the following:
#        1.  Highest value for a specific column for all cities
#        2.  Lowest value for a specific column for all cities
#        3.  Average value for a specific column for all cities
#        4.  Modes for a specific column for all cities
#        5.  Summary Statistics for a specific column for a specific city
#        6.  High and low averages for each category across all data
#        7.  Quit
#    5.  Repeat steps 3 and 4 until the user chooses to quit
#    6.  Print a goodbye message
###########################################################

import csv
from typing import Any, List, Tuple, TextIO, Union
from datetime import datetime
from operator import itemgetter

COLUMNS = [
    "date",
    "average temp",
    "high temp",
    "low temp",
    "precipitation",
    "snow",
    "snow depth",
]
TOL = 0.02
BANNER = "This program will take in csv files with weather data and compare \
the sets.\nThe data is available for high, low, and average temperatures,\
\nprecipitation, and snow and snow depth."
MENU = """
        Menu Options:
        1. Highest value for a specific column for all cities
        2. Lowest value for a specific column for all cities
        3. Average value for a specific column for all cities
        4. Modes for a specific column for all cities
        5. Summary Statistics for a specific column for a specific city
        6. High and low averages for each category across all data
        7. Quit
        Menu Choice: """


def open_files() -> Union[List[str], List[TextIO]]:
    """
    This function will open the files that the user inputs and return a list of
    the file names and a list of the file pointers.
    """
    while True:
        cities = []
        cities_fp = []
        str_list = input("Enter cities names: ")
        str_list = str_list.strip()
        str_list = str_list.split(",")
        for city in str_list:
            try:
                # Strip whitespace from city name, open file, and append to
                # list of cities and list of file pointers
                city = city.strip()
                city_fp = open(city + ".csv", "rt")
                cities.append(city)
                cities_fp.append(city_fp)\
            # If the file is not found, print an error message and continue
            except FileNotFoundError:
                print(f"\nError: File {city}.csv is not found")
                continue
        return cities, cities_fp


def null_float(value: str) -> float:
    """
    This function will return None if the value is an empty string, otherwise
    it will return the float value of the string.
    """
    if value == "":
        return None
    else:
        return float(value)


def read_files(
    cities_fp: List[TextIO],
) -> List[List[Tuple[str, float, float, float, float, float, float]]]:
    """
    This function will read the file pointers 
    and return a list of lists of tuples, containing the data within the files.
    """
    output = []
    # For each file pointer, read the file and append the data to the output
    for fp in cities_fp:
        data = []
        reader = csv.reader(fp)
        # Skip the first two rows (headers)
        next(reader)
        next(reader)
        for row in reader:
            # Convert the date to a datetime object and the rest of the values
            # to floats, checking for empty strings
            date = row[0]
            average_temp = null_float(row[1])
            high_temp = null_float(row[2])
            low_temp = null_float(row[3])
            precipitation = null_float(row[4])
            snow = null_float(row[5])
            snow_depth = null_float(row[6])
            data.append(
                (
                    date,
                    average_temp,
                    high_temp,
                    low_temp,
                    precipitation,
                    snow,
                    snow_depth,
                )
            )
        output.append(data)
    return output


def get_data_in_range(
    master_list: List[
        List[Tuple[str, float, float, float, float, float, float]]
    ],
    start_str: str,
    end_str: str,
) -> List[List[Tuple[str, float, float, float, float, float, float]]]:
    """
    This function will return a list of lists of tuples, containing the data
    within the files, but only for the dates between the start and end dates.
    """
    start_date = datetime.strptime(start_str, "%m/%d/%Y").date()
    end_date = datetime.strptime(end_str, "%m/%d/%Y").date()
    output = []
    for i in range(len(master_list)):
        output.append([])
        for row in master_list[i]:
            date = datetime.strptime(row[0], "%m/%d/%Y").date()
            # If the date is within the range, append it to the output
            if date >= start_date and date <= end_date:
                output[i].append(row)
    return output


def get_min(
    col: int,
    data: List[List[Tuple[str, float, float, float, float, float, float]]],
    cities: List[str],
) -> Tuple[str, float]:
    """
    This function will return a tuple containing the city with the lowest value
    for the specified column and the value.
    """
    min_values = []
    for city in data:
        sanitized_city = []
        for row in city:
            # If the value is not None, append it to the sanitized_city
            if row[col] != None:
                sanitized_city.append(row[col])
        # Append the minimum value of the sanitized_city
        # to the list of minimum values
        min_values.append(min(sanitized_city))
    output = []
    # For each city, append a tuple containing the city name and the minimum
    for city in cities:
        output.append((city, min_values[cities.index(city)]))
    return output


def get_max(
    col: int,
    data: List[List[Tuple[str, float, float, float, float, float, float]]],
    cities: List[str],
) -> Tuple[str, float]:
    """
    This function will return a tuple containing the city with the highest value
    for the specified column and the value.
    """
    max_values = []
    for city in data:
        # Sanitize the data by removing None values
        sanitized_city = []
        for row in city:
            if row[col] != None:
                sanitized_city.append(row[col])
        # Append the maximum value of the sanitized_city
        max_values.append(max(sanitized_city))
    output = []
    for city in cities:
        output.append((city, max_values[cities.index(city)]))
    return output


def average(lst: List[float]) -> float:
    """
    This function will return the average of a list of numbers.
    """
    return sum(lst) / len(lst)


def tol_eq(a: float, b: float) -> bool:
    """
    This function will return True if the absolute value of the difference
    between a and b divided by a is less than TOL, otherwise it will return
    False.
    """
    if a != 0:
        return abs((a - b) / a) < TOL
    else:
        return False


def remove_duplicates(lst: List[Any]) -> List[Any]:
    """
    This function will return a list with all duplicates removed.
    """
    output = []
    for i in lst:
        if i not in output:
            output.append(i)
    return output


def multi_max(lst: List[Tuple[Any, float]]) -> List[Any]:
    """
    This function will return a list of all the values in lst that are equal
    to the maximum value in lst.
    """
    output = []
    max_value = max(lst, key=itemgetter(1))[1]
    for i in lst:
        # If the value is equal to the maximum value, append it to the output
        if i[1] == max_value:
            output.append(i[0])
    return output


def mode(lst: List[Any]) -> Tuple[List[Any], int]:
    """
    This function will return a list of the mode(s) of lst and the number of
    times the mode(s) occur.
    """
    lst = sorted(lst)
    counts = []
    streak_num = lst[0]
    streak_count = 1
    for i in range(1, len(lst)):
        # Check if the current value is the last value in lst
        if i == len(lst) - 1:
            if tol_eq(lst[i], streak_num):
                streak_count += 1
            counts.append((streak_num, streak_count))
        # Check if the current value is equal to the streak number
        # and increment the streak count if it is
        elif tol_eq(lst[i], streak_num):
            streak_count += 1
        # If the current value is not equal to the streak number,
        # append the streak number and streak count to the counts list
        else:
            counts.append((streak_num, streak_count))
            streak_num = lst[i]
            streak_count = 1
    # Return the mode(s) and the number of times they occur
    return multi_max(counts), max(counts, key=itemgetter(1))[1]


def get_average(
    col: int,
    data: List[List[Tuple[str, float, float, float, float, float, float]]],
    cities: List[str],
) -> Tuple[str, float]:
    """
    This function will return a tuple containing the city with the highest value
    for the specified column and the value.
    """
    average_values = []
    for city in data:
        tot = 0
        count = 0
        for row in city:
            # If the value is None, skip it
            if row[col] == None:
                continue
            # If the value is not None, add it to the total and increment the count
            else:
                tot += float(row[col])
                count += 1
        # Append the average of the values in the city to the list of averages
        # and round it to two decimal places
        average_values.append(round(tot / count, 2))
    output = []
    # For each city, append a tuple containing the city name and the average
    for city in cities:
        output.append((city, average_values[cities.index(city)]))
    return output


def get_modes(
    col: int,
    data: List[List[Tuple[str, float, float, float, float, float, float]]],
    cities: List[str],
) -> Tuple[str, float]:
    """
    This function will return a tuple containing the city with the highest value
    for the specified column and the value.
    """
    mode_values = []
    for city in data:
        sanitized_city = []
        # Sanitize the data by removing None values
        for row in city:
            if row[col] != None:
                sanitized_city.append(row[col])
        # Append the mode of the sanitized_city
        mode_values.append(mode(sanitized_city))
    output = []
    # For each city, append a tuple containing the city name and the mode
    for city in cities:
        # If the mode only occurs once, append an empty list as the mode
        if mode_values[cities.index(city)][1] == 1:
            output.append((city, [], mode_values[cities.index(city)][1]))
        # If the mode occurs more than once, append the mode
        else:
            output.append(
                (
                    city,
                    mode_values[cities.index(city)][0],
                    mode_values[cities.index(city)][1],
                )
            )
    return output


def high_low_averages(data, cities, categories):
    """
    This function will return a list of tuples containing the city with the
    lowest value for the specified column and the value, and the city with the
    highest value for the specified column and the value.
    """
    output = []
    for category in categories:
        try:
            col = COLUMNS.index(category)
            averages = get_average(col, data, cities)
            averages = sorted(averages, key=itemgetter(1))
            # grab all max values, so that if there are multiple max values,
            # the first instance can be returned
            max_values = []
            for i in range(len(averages)):
                if averages[i][1] == averages[-1][1]:
                    max_values.append(averages[i])
            # append the lowest and highest values to the output list
            output.append(
                [
                    (averages[0][0], round(averages[0][1], 2)),
                    (max_values[0][0], round(max_values[0][1], 2)),
                ]
            )
        # If the category is not in COLUMNS, append None
        except ValueError:
            output.append(None)
    return output


def display_statistics(col, data, cities):
    """
    This function will print the statistics for the specified column.
    """
    # Get the statistics for the specified column
    averages = get_average(col, data, cities)
    modes = get_modes(col, data, cities)
    mins = get_min(col, data, cities)
    maxs = get_max(col, data, cities)
    # Print the statistics
    print(f"\n\t{COLUMNS[col]}: ")
    for i in range(len(cities)):
        print(f"\t{cities[i]}: ")
        print(
            f"\tMin: {mins[i][1]:.2f} Max: {maxs[i][1]:.2f}",
            f"Avg: {averages[i][1]:.2f}"
        )
        # If the mode only occurs once, print that there are no modes
        if modes[i][2] == 1:
            print(f"\tNo modes.")
        else:
            print(
                f"\tMost common repeated values ({modes[i][2]} occurrences):",
                f"{str(*modes[i][1])}\n"
            )


def get_user_input(in_data):
    """
    This function will get the user input for the desired category and date
    range.
    """
    # Get the user input for the desired category and date range
    start_date = input("\nEnter a starting date (in mm/dd/yyyy format): ")
    end_date = input("\nEnter an ending date (in mm/dd/yyyy format): ")
    # Error handle for the category
    while True:
        category = input("\nEnter desired category: ").lower()
        if category in COLUMNS:
            col = COLUMNS.index(category)
            data = get_data_in_range(in_data, start_date, end_date)
            return data, category, col
        else:
            print(f"\n\t{category} category is not found.")
            continue


def main():
    """
    This is the main function, handling the menu and calling the other
    functions.
    """
    print(BANNER)
    cities, cities_fp = open_files()
    data = read_files(cities_fp)
    while True:
        choice = int(input(MENU))
        if choice == 1:
            # Get the user input for the desired category and date range
            master, category, col = get_user_input(data)
            maxs = get_max(col, master, cities)
            print(f"\n\t{category}: ")
            # Print the max values
            for i in maxs:
                print(f"\tMax for {i[0]:s}: {i[1]:.2f}")
        elif choice == 2:
            # Get the user input for the desired category and date range
            master, category, col = get_user_input(data)
            mins = get_min(col, master, cities)
            print(f"\n\t{category}: ")
            # Print the min values
            for i in mins:
                print(f"\tMin for {i[0]:s}: {i[1]:.2f}")
        elif choice == 3:
            # Get the user input for the desired category and date range
            master, category, col = get_user_input(data)
            avgs = get_average(col, master, cities)
            print(f"\n\t{category}: ")
            # Print the average values
            for i in avgs:
                print(f"\tAverage for {i[0]:s}: {i[1]:.2f}")
        elif choice == 4:
            # Get the user input for the desired category and date range
            master, category, col = get_user_input(data)
            modes = get_modes(col, master, cities)
            print(f"\n\t{category}: ")
            # Print the mode values
            for i in modes:
                print(
                    f"\tMost common repeated values for {i[0]:s} ({i[2]}",
                    f"occurrences): {str(*i[1])}\n"
                )
        elif choice == 5:
            # Get the user input for the desired category and date range
            # and display the statistics
            # DATA is a constant here because some functions attempt to modify
            # the data, so a constant is made to prevent that
            DATA, category, col = get_user_input(data)
            display_statistics(col, DATA, cities)
        elif choice == 6:
            # here the function isn't used as the categories can be entered
            # by the user in comma seperated format
            start_date = input(
                "\nEnter a starting date (in mm/dd/yyyy format): "
            )
            end_date = input("\nEnter an ending date (in mm/dd/yyyy format): ")
            # Error handle for the category
            categories = (
                input("\nEnter desired categories seperated by comma: ")
                .lower()
                .split(",")
            )
            # Get the data in the specified date range, and assign DATA as a 
            # constant to prevent modification
            DATA = get_data_in_range(data, start_date, end_date)
            category_avgs = high_low_averages(DATA, cities, categories)
            # Print the high and low averages for each category
            print("\nHigh and low averages for each category across all data.")
            count = 0
            for category in category_avgs:
                if category != None:
                    print(f"\n\t{categories[count]}: ")
                    print(
                        f"\tLowest Average: {category[0][0]} =",
                        f"{category[0][1]:.2f} Highest Average:",
                        f"{category[1][0]} = {category[1][1]:.2f}"
                    )
                else:
                    print(f"\n\t{categories[count]} category is not found.")
                count += 1
        elif choice == 7:
            print("\nThank you using this program!")
            break


if __name__ == "__main__":
    main()
