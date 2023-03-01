import csv
from typing import Tuple, IO
import os
from operator import itemgetter

TITLE = 1
AUTHOR = 2
CATEGORY = 3
DESCRIPTION = 4
YEAR = 5
RATING = 6
PAGES = 7

MENU = "\nWelcome to the Book Recommendation Engine\n\
        Choose one of below options:\n\
        1. Find a book with a title\n\
        2. Filter books by a certain criteria\n\
        3. Recommend a book \n\
        4. Quit the program\n\
        Enter option: "

CRITERIA_INPUT = "\nChoose the following criteria\n\
                 (3) Category\n\
                 (5) Year Published\n\
                 (6) Average Rating (or higher) \n\
                 (7) Page Number (within 50 pages) \n\
                 Enter criteria number: "

def open_file() -> IO:
    ''' open file and return file pointer'''
    while True:
        filename = input("\nEnter filename: ")
        filepath = os.path.join(os.path.dirname(__file__), filename)
        try:
            fp = open(filepath, "r", encoding="utf-8")
        except:
            print("\nFile not found!")
            continue
        return fp


def read_file(fp: IO) -> list[Tuple]:
    """Docstring"""
    output = []
    reader = csv.reader(fp, delimiter=',')
    #skip first line:
    next(reader)
    for line in reader:
        output.append((line[0], line[2], line[4], line[5].lower().split(","), line[7], line[8], float(line[9]), int(line[10]), int(line[11])))
    return output


def get_books_by_criterion(list_of_tuples: list[Tuple], criterion: int, value: int | float | str) -> list[Tuple] | Tuple:
    """Docstring"""
    output = []
    if criterion == TITLE:
        for book in list_of_tuples:
            if value.lower() == book[TITLE].lower():
                return book
    elif criterion == CATEGORY:
        for book in list_of_tuples:
            if value.lower() in book[CATEGORY]:
                output.append(book)
        return output
    elif criterion == YEAR:
        for book in list_of_tuples:
            if value == book[YEAR]:
                output.append(book)
        return output
    elif criterion == RATING:
        for book in list_of_tuples:
            if value <= book[RATING]:
                print(book[RATING])
                output.append(book)
        return output
    elif criterion == PAGES:
        for book in list_of_tuples:
            if (value - 50) <= book[PAGES] <= (value + 50):
                output.append(book)
        return output
    return []


def get_books_by_criteria(list_of_tuples: list[Tuple], category: str, rating: float, pages: int):
    """Docstring"""
    output = get_books_by_criterion(list_of_tuples, CATEGORY, category)
    output = get_books_by_criterion(output, RATING, rating)
    output = get_books_by_criterion(output, PAGES, pages)
    return output


def get_books_by_keyword(list_of_tuples, keywords):
    output = []
    for book in list_of_tuples:
        for keyword in keywords:
            if keyword.lower() in book[DESCRIPTION].lower():
                output.append(book)
                break
    return output


def recommend_books(list_of_tuples: list[Tuple], keywords, category, rating, page_number, a_z: bool) -> list[Tuple]:
    """Docstring"""
    output = get_books_by_keyword(list_of_tuples, keywords)
    output = get_books_by_criteria(output, category, rating, page_number)
    output = sort_authors(output, a_z)
    return output


def sort_authors(list_of_tuples, a_z=True) -> list[Tuple]:
    output = list_of_tuples.copy()
    output.sort(key=itemgetter(AUTHOR), reverse=not a_z)
    return output


def main():
    fp = open_file()
    list_of_tuples = read_file(fp)
    print(list_of_tuples)


# DO NOT CHANGE THESE TWO LINES
# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.
if __name__ == "__main__":
    main()
