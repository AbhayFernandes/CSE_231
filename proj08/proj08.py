###########################################################
#  Computer Project #7
#  Algorithm
#    1. 
###########################################################


import csv
import datetime
from operator import itemgetter


MENU = """\nSelect from the option: 
        1.Games in a certain year 
        2. Games by a Developer 
        3. Games of a Genre 
        4. Games by a developer in a year 
        5. Games of a Genre with no discount 
        6. Games by a developer with discount 
        7. Exit 
        Option: """


def open_file(s):
    while True:
        try:
            fp_games = open(input(f"\nEnter {s} file: "), "r")
            return fp_games
        except FileNotFoundError:
            print("\nNo Such file")


def read_file(fp_games):
    """
    This function reads the file and returns a dictionary with the game ID as
    the key and the rest of the information as a list.
    """
    reader = csv.reader(fp_games)
    next(reader)
    master_D = {}
    for row in reader:
        # check if game is single or multi-player
        if row[4].split(";")[0].lower() == "multi-player":
            mode = 0
        else:
            mode = 1
        # convert price to USD
        try:
            price = float(row[5].replace(",", "")) * 0.012
        except ValueError:
            price = 0.0
        supports = []
        # check if game supports windows, mac, or linux
        if row[9] == "1":
            supports.append("win_support")
        if row[10] == "1":
            supports.append("mac_support")
        if row[11] == "1":
            supports.append("lin_support")
        # add game to master dictionary
        master_D[row[0]] = [
            row[1],
            row[2].split(";"),
            row[3].split(";"),
            mode,
            price,
            row[6],
            int(row[7]),
            int(row[8][:-1]),
            supports,
        ]
    return master_D


def read_discount(fp_discount):
    """
    This function reads the discount file and returns a dictionary with the
    game ID as the key and the discount as the value.
    """
    reader = csv.reader(fp_discount)
    next(reader)
    discount_D = {}
    for row in reader:
        # add game to discount dictionary, round discount to 2 decimal places
        discount_D[row[0]] = round(float(row[1]), 2)
    return discount_D


def in_year(master_D, year):
    """
    This function takes in a dictionary and a year and returns a list of games
    that were released in that year.
    """
    # convert int supplied into a datetime year
    year = datetime.datetime.strptime(str(year), "%Y").year
    output = []
    for game in master_D.keys():
        # convert release date into a datetime year
        release = datetime.datetime.strptime(master_D[game][0], "%d/%m/%Y").year
        # check if release year matches year supplied
        if release == year:
            output.append(game)
    return sorted(output)


def by_genre(master_D, genre):
    """
    This function takes in a dictionary and a genre and returns a list of games
    that are of that genre.
    """
    matches = []
    positive_reviews = []
    # create a list of games that match the genre supplied
    for game in master_D.keys():
        if genre in master_D[game][2]:
            matches.append(game)
    # create a list of the percent positive reviews for each game, matching
    # index of the games list above to allow for sorting
    for game in matches:
        positive_reviews.append(master_D[game][7])
    return double_list_sort(positive_reviews, matches, reverse=True)


def by_dev(master_D, developer):
    """
    This function takes in a dictionary of games
    and a developer string, and returns a list of
    games that were developed by that developer.
    """
    matches = []
    dates = []
    # create a list of games that match the developer supplied
    for game in master_D.keys():
        if developer in master_D[game][1]:
            matches.append(game)
    # create a list of the release dates for each game, matching
    # index of the games list above to allow for sorting
    for game in matches:
        dates.append(
            datetime.datetime.strptime(master_D[game][0], "%d/%m/%Y").year
        )
    return double_list_sort(dates, matches, reverse=True)


def per_discount(master_D, games, discount_D):
    """
    This function takes in a dictionary of games, a list of games, and a
    dictionary of discounts and returns a list of prices for each game in the
    list, with the discount applied.
    """
    output = []
    for game in games:
        try:
            output.append(
                round(master_D[game][4] * (1 - (discount_D[game] / 100)), 6)
            )
        except KeyError:
            output.append(round(master_D[game][4], 6))
    return output


def double_list_sort(list1, list2, reverse=False):
    """
    This function takes in two lists and a boolean value and returns a list
    of the second list sorted by the first list.
    """
    output = []
    for i in range(len(list1)):
        output.append([list1[i], list2[i]])
    output = sorted(output, key=itemgetter(0), reverse=reverse)
    for i in range(len(output)):
        output[i] = output[i][1]
    return output


def by_dev_year(master_D, discount_D, developer, year):
    """
    This function takes in a dictionary of games, a dictionary of discounts,
    a developer string, and a year and returns a list of games that were
    developed by that developer and released in that year, sorted by price.
    """
    dev_games = by_dev(master_D, developer)
    year_games = in_year(master_D, year)
    # find games that are in both lists, using set intersection
    matches = sorted(list(set(dev_games) & set(year_games)))
    prices = per_discount(master_D, matches, discount_D)
    # sort by price of game:
    return double_list_sort(prices, matches, reverse=False)


def by_genre_no_disc(master_D, discount_D, genre):
    """
    This function takes in a dictionary of games, a dictionary of discounts,
    and a genre string and returns a list of games that are of that genre
    and are not on discount, sorted by percent positive reviews.
    """
    genres = by_genre(master_D, genre)
    matches = []
    for game in genres:
        # check if game is not in discount dictionary, if so add to matches
        if game not in discount_D.keys():
            matches.append(game)
    # sort by percent positive reviews:
    percent_positive_reviews = [master_D[game][7] for game in matches]
    matches = double_list_sort(percent_positive_reviews, matches, reverse=True)
    # then by price of game, allowing ties to be settled by previous sort.
    prices = per_discount(master_D, matches, discount_D)
    return double_list_sort(prices, matches, reverse=False)


def by_dev_with_disc(master_D, discount_D, developer):
    """
    This function takes in a dictionary of games, a dictionary of discounts,
    and a developer string and returns a list of games that were developed
    by that developer and are on discount, sorted by price.
    """
    matches = by_dev(master_D, developer)
    output = []
    for game in matches:
        # check if game is in discount dictionary, if so add to output
        if game in discount_D.keys():
            output.append(game)
    # sort by price of game:
    prices = per_discount(master_D, output, discount_D)
    dates = []
    for game in output:
        dates.append(
            datetime.datetime.strptime(master_D[game][0], "%d/%m/%Y").year
        )
    # sort by release date, allowing ties to be settled by previous sort.
    output = double_list_sort(dates, output, reverse=False)
    return double_list_sort(prices, output, reverse=True)


def output_list_with_commas(lst):
    """
    This function takes in a list and prints it with commas between each,
    checking if the last element is reached and printing an ending instead.
    """
    if lst:
        for game in lst:
            # check if last element
            if game == lst[-1]:
                print(f"{game}")
            else:
                print(f"{game}, ", end="")
    else:
        print(f"\nNothing to print")


def main():
    """
    This function is the main function of the program, and handles the
    user interface.
    """
    games = read_file(open_file("games"))
    discount = read_discount(open_file("discount"))
    while True:
        option = input(MENU)
        if option == "1":
            # check if input is a valid year
            while True:
                try:
                    year = int(input("\nWhich year: "))
                    break
                except ValueError:
                    print("\nPlease enter a valid year")
            matches = in_year(games, year)
            if matches != []:
                print(f"\nGames released in {year}:")
            output_list_with_commas(matches)
        elif option == "2":
            developer = input("\nWhich developer: ")
            matches = by_dev(games, developer)
            if matches != []:
                print(f"\nGames made by {developer}:")
            output_list_with_commas(matches)
        elif option == "3":
            genre = input("\nWhich genre: ")
            matches = by_genre(games, genre)
            if matches != []:
                print(f"\nGames with {genre} genre:")
            output_list_with_commas(matches)
        elif option == "4":
            developer = input("\nWhich developer: ")
            # check if input is a valid year
            while True:
                try:
                    year = int(input("\nWhich year: "))
                    break
                except ValueError:
                    print("\nPlease enter a valid year")
            matches = by_dev_year(games, discount, developer, year)
            if matches != []:
                print(f"\nGames made by {developer} and released in {year}:")
            output_list_with_commas(matches)
        elif option == "5":
            genre = input("\nWhich genre: ")
            matches = by_genre_no_disc(games, discount, genre)
            if matches != []:
                print(f"\nGames with {genre} genre and without a discount:")
            output_list_with_commas(matches)
        elif option == "6":
            developer = input("\nWhich developer: ")
            matches = by_dev_with_disc(games, discount, developer)
            if matches != []:
                print(f"\nGames made by {developer} which offer discount:")
            output_list_with_commas(matches)
        elif option == "7":
            print("\nThank you.")
            break
        else:
            print("\nInvalid option")


if __name__ == "__main__":
    main()
