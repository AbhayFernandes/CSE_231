import csv
from operator import itemgetter

TITLE = 1
CATEGORY = 3
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

def open_file():
    """Docstring"""
    pass

def read_file(fp):
    """Docstring"""
    pass

def get_books_on_criterion(list_of_tuples, criterion, value):
    """Docstring"""
    pass

def get_books_by_criteria(list_of_tuples, category, rating, page_number):
    """Docstring"""
    pass

def get_books_by_keyword(list_of_tuples, keywords):
    """Docstring"""
    pass

def sort_authors(list_of_tuples, a_z):
    """Docstring"""
    pass

def recommend_books(list_of_tuples, keywords, category, rating, page_number,  a_z):
    """Docstring"""
    pass

def display_books(list_of_tuples):
    """Docstring"""
    pass

def get_option():
    """Docstring"""
    pass

def main():
    pass


# DO NOT CHANGE THESE TWO LINES
# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.
if __name__ == "__main__":
    main()
