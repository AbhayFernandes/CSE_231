import csv
from typing import List, Tuple, IO, Union
from typing import List, Tuple, IO, Union
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
    """open a file and return file pointer"""
    while True:
        # get file name from user
        filename = input("Enter file name: ")
        filepath = os.path.join(os.path.dirname(__file__), filename)
        # open file
        try:
            fp = open(filepath, "r", encoding="utf-8")
        # handle error
        except IOError:
            print("\nError opening file. Please try again.")
            continue
        return fp


def read_file(fp: IO) -> list[Tuple]:
    """Docstring"""
    output = []
    reader = csv.reader(fp, delimiter=",")
    # skip first line:
    next(reader)
    for line in reader:
        try:
            # append tuple to output list
            output.append(
                (
                    line[0],
                    line[2],
                    line[4],
                    line[5].lower().split(","),
                    line[7],
                    line[8],
                    float(line[9]),
                    int(line[10]),
                    int(line[11]),
                )
            )
        except ValueError:
            continue
    return output


def get_books_by_criterion(
    list_of_tuples: List[Tuple], criterion: int, value: Union[int, float, str]
) -> Union[List[Tuple], Tuple]:
    """return a list of tuples that match the criterion and value"""
    output = []
    if criterion == TITLE:
        # search for title
        for book in list_of_tuples:
            if value.lower() == book[TITLE].lower():
                return book
    elif criterion == CATEGORY:
        # search for category
        for book in list_of_tuples:
            if value.lower() in book[CATEGORY]:
                output.append(book)
        return output
    elif criterion == YEAR:
        # search for year
        for book in list_of_tuples:
            if value == book[YEAR]:
                output.append(book)
        return output
    elif criterion == RATING:
        # search for rating
        for book in list_of_tuples:
            if value <= book[RATING]:
                output.append(book)
        return output
    elif criterion == PAGES:
        # search for pages
        for book in list_of_tuples:
            if (value - 50) <= book[PAGES] <= (value + 50):
                output.append(book)
        return output
    return []


def get_books_by_criteria(
    list_of_tuples: List[Tuple], category: str, rating: float, pages: int
):
    """return a list of tuples that match the various different criteria"""
    output = get_books_by_criterion(list_of_tuples, CATEGORY, category)
    output = get_books_by_criterion(output, RATING, rating)
    output = get_books_by_criterion(output, PAGES, pages)
    return output


def get_books_by_keyword(list_of_tuples, keywords):
    """return a list of tuples that match the keywords"""
    output = []
    for book in list_of_tuples:
        for keyword in keywords:
            if keyword.lower() in book[DESCRIPTION].lower():
                output.append(book)
                break
    return output


def recommend_books(
    list_of_tuples: List[Tuple],
    keywords,
    category,
    rating,
    page_number,
    a_z: bool,
) -> List[Tuple]:
    """return a list of tuples that match the criteria and keywords"""
    output = get_books_by_criteria(
        list_of_tuples, category, rating, page_number
    )
    output = get_books_by_keyword(output, keywords)
    output = sort_authors(output, a_z)
    return output


def sort_authors(list_of_tuples, a_z=True) -> List[Tuple]:
    """return a list of tuples sorted by author"""
    output = list_of_tuples.copy()
    output.sort(key=itemgetter(AUTHOR), reverse=not a_z)
    return output


def display_books(list_of_tuples: List[Tuple]) -> None:
    """print the books in a nice format"""
    print("\nBook Details:")
    # check if list is empty
    if len(list_of_tuples) == 0:
        print("Nothing to print.")
        return
    # print header
    print(
        "{:15s} {:35s} {:35s} {:6s} {:8s} {:15s} {:15s}".format(
            "ISBN-13",
            "Title",
            "Authors",
            "Year",
            "Rating",
            "Number Pages",
            "Number Ratings",
        )
    )
    for book in list_of_tuples:
        # check if title or author is too long
        if len(book[TITLE]) > 35 or len(book[AUTHOR]) > 35:
            continue
        # print book details
        print(
            "{:15s} {:35s} {:35s} {:6s} {:<8.2f} {:<15d} {:<15d}".format(
                book[0],
                book[TITLE],
                book[AUTHOR],
                book[YEAR],
                float(book[RATING]),
                int(book[PAGES]),
                int(book[8]),
            )
        )


def get_option() -> int:
    """get a valid option from the user"""
    while True:
        user_choice = input(MENU)
        try:
            # check if user choice is valid
            return int(user_choice)
        except ValueError:
            # handle error
            print("\nInvalid input")
            continue


def get_valid_int(prompt: str) -> int:
    """get a valid int from the user"""
    while True:
        # get user input
        user_input = input(prompt)
        try:
            # check if user input is valid
            return int(user_input)
        except ValueError:
            # handle error
            print("\nInvalid input")
            continue


def get_valid_float(prompt: str) -> float:
    """get a valid float from the user"""
    while True:
        # get user input
        user_input = input(prompt)
        try:
            # check if user input is valid
            return float(user_input)
        except ValueError:
            # handle error
            print("\nInvalid input")
            continue


def display_books(list_of_tuples: List[Tuple]) -> None:
    """print the books in a nice format"""
    print("\nBook Details:")
    # check if list is empty
    if len(list_of_tuples) == 0:
        print("Nothing to print.")
        return
    # print header
    print(
        "{:15s} {:35s} {:35s} {:6s} {:8s} {:15s} {:15s}".format(
            "ISBN-13",
            "Title",
            "Authors",
            "Year",
            "Rating",
            "Number Pages",
            "Number Ratings",
        )
    )
    for book in list_of_tuples:
        # check if title or author is too long
        if len(book[TITLE]) > 35 or len(book[AUTHOR]) > 35:
            continue
        # print book details
        print(
            "{:15s} {:35s} {:35s} {:6s} {:<8.2f} {:<15d} {:<15d}".format(
                book[0],
                book[TITLE],
                book[AUTHOR],
                book[YEAR],
                float(book[RATING]),
                int(book[PAGES]),
                int(book[8]),
            )
        )


def get_option() -> int:
    """get a valid option from the user"""
    while True:
        user_choice = input(MENU)
        try:
            # check if user choice is valid
            return int(user_choice)
        except ValueError:
            # handle error
            print("\nInvalid input")
            continue


def get_valid_int(prompt: str) -> int:
    """get a valid int from the user"""
    while True:
        # get user input
        user_input = input(prompt)
        try:
            # check if user input is valid
            return int(user_input)
        except ValueError:
            # handle error
            print("\nInvalid input")
            continue


def get_valid_float(prompt: str) -> float:
    """get a valid float from the user"""
    while True:
        # get user input
        user_input = input(prompt)
        try:
            # check if user input is valid
            return float(user_input)
        except ValueError:
            # handle error
            print("\nInvalid input")
            continue


def display_books(list_of_tuples: List[Tuple]) -> None:
    print("\nBook Details:")
    if len(list_of_tuples) == 0:
        print("Nothing to print.")
        return
    print("{:15s} {:35s} {:35s} {:6s} {:8s} {:15s} {:15s}".format("ISBN-13", "Title", "Authors", "Year", "Rating", "Number Pages", "Number Ratings"))
    for book in list_of_tuples:
        if len(book[TITLE]) > 35 or len(book[AUTHOR]) > 35:
            continue
        print("{:15s} {:35s} {:35s} {:6s} {:<8.2f} {:<15d} {:<15d}".format(book[0], book[TITLE], book[AUTHOR], book[YEAR], float(book[RATING]), int(book[PAGES]), int(book[8])))


def get_option() -> int:
    while True:
        user_choice = input(MENU)
        try:
            return int(user_choice)
        except ValueError:
            print("\nInvalid input")
            continue
        if int(user_choice) not in range(1, 5):
            print("\nInvalid input")
            continue


def get_valid_int(prompt: str) -> int:
    while True:
        user_input = input(prompt)
        try:
            return int(user_input)
        except ValueError:
            print("\nInvalid input")
            continue


def get_valid_float(prompt: str) -> float:
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print("\nInvalid input")
            continue

def main():
    """
    This program starts by reading a file of books.
    it then allows the user to search for books by title, category, year,
    rating, and number of pages.
    This program also allows the user to search for:
    by keywords in the description, by author.
    The user can also print the books in a nice format.
    """
    fp = open_file()
    list_of_tuples = read_file(fp)
    while True:
        # get user choice
        user_choice = get_option()
        if user_choice == 1:
            # search for title
            title = input("\nInput a book title: ")
            book = get_books_by_criterion(list_of_tuples, TITLE, title)
            # check if book is found
            if book:
                # print book details
                print("\nBook Details:")
                print(
                    "{:15s} {:35s} {:35s} {:6s} {:8s} {:15s} {:15s}".format(
                        "ISBN-13",
                        "Title",
                        "Authors",
                        "Year",
                        "Rating",
                        "Number Pages",
                        "Number Ratings",
                    )
                )
                print(
                    "{:15s} {:35s} {:35s} {:6s} {:<8.2f} {:<15d} {:<15d}".format(
                        book[0],
                        book[TITLE],
                        book[AUTHOR],
                        book[YEAR],
                        float(book[RATING]),
                        int(book[PAGES]),
                        int(book[8]),
                    )
                )
            else:
                # handle error
                print("No book found")
        # search for books by criteria
        elif user_choice == 2:
            while True:
                try:
                    # get criterion
                    criterion = int(input(CRITERIA_INPUT))
                    if criterion not in [3, 5, 6, 7]:
                        print("\nInvalid input")
                        continue
                    break
                except ValueError:
                    # handle error
                    print("\nInvalid input")
            if criterion == 3:
                # get category
                value = input("\nEnter value: ")
            elif criterion == 5:
                # get year
                value = input("\nEnter value: ")
            elif criterion == 6:
                # get rating
                value = get_valid_float(prompt="\nEnter value: ")
            elif criterion == 7:
                # get number of pages
                value = get_valid_int(prompt="\nEnter value: ")
            # get books by criterion
            books = get_books_by_criterion(list_of_tuples, criterion, value)
            books = sort_authors(books)
            display_books(books[:30])
        elif user_choice == 3:
            # get books by criteria, ask for data
            category = input("\nEnter the desired category: ")
            rating = float(input("\nEnter the desired rating: "))
            pages = int(input("\nEnter the desired page number: "))
            a_z = input("\nEnter 1 for A-Z sorting, and 2 for Z-A sorting: ")
            # check if user input is valid, then assign boolean values
            if a_z.lower() == "1":
                a_z = True
            elif a_z.lower() == "2":
                a_z = False
            # get books by criteria
            keywords = input("\nEnter keywords (space separated): ").split(" ")
            books = recommend_books(
                list_of_tuples, keywords, category, rating, pages, a_z
            )
            # check if books are found
            display_books(books)
        elif user_choice == 4:
            break
        else:
            print("\nInvalid option")


# DO NOT CHANGE THESE TWO LINES
# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.
if __name__ == "__main__":
    main()
