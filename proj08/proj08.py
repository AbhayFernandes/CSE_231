import csv
from operator import itemgetter


MENU = '''\nSelect from the option:
        1.Games in a certain year
        2. Games by a Developer
        3. Games of a Genre
        4. Games by a developer in a year
        5. Games of a Genre with no discount
        6. Games by a developer with discount
        7. Exit
        Option: '''


def open_file(s):
    while True:
        try:
            fp = open(s, encoding='utf-8')
            return fp
        except FileNotFoundError:
            print('File not found. Please try again.')


def read_file(fp_games):
    ''' Docstring'''
    pass   # remove this line


def read_discount(fp_discount):
    ''' Docstring'''
    pass   # remove this line


def in_year(master_D, year):
    ''' Docstring'''
    pass   # remove this line


def by_genre(master_D, genre):
    ''' Docstring'''
    pass   # remove this line


def by_dev(master_D, developer):
    ''' Docstring'''
    pass   # remove this line


def per_discount(master_D, games, discount_D):
    ''' Docstring'''
    pass   # remove this line


def by_dev_year(master_D, discount_D, developer, year):
    ''' Docstring'''
    pass   # remove this line


def by_genre_no_disc(master_D, discount_D, genre):
    ''' Docstring'''
    pass   # remove this line


def by_dev_with_disc(master_D, discount_D, developer):
    ''' Docstring'''
    pass   # remove this line


def main():
    pass   # remove this line


if __name__ == "__main__":
    main()
