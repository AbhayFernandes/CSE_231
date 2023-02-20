''' Insert heading comments here.'''
from typing import Tuple, IO
import os

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
    pass  # insert your code here
    
def find_max(num: float, name: str, max_num: str, max_name: str) -> Tuple[float, str]:
    ''' find the max number and return the max number and the name of the max number'''
    if num < max_num:
        return max_num, max_name
    elif num > max_num:
        return num, f"\n\t{name}"
    else:
        return max_num, f"{max_name}\n\t{name}"

    
def find_min(num: float, name: str, min_num: float, min_name: str) -> Tuple[float, str]:
    ''' find the min number and return the min number and the name of the min number'''
    if num > min_num:
        return min_num, min_name
    elif num < min_num:
        return num, f"\n\t{name}"
    else:
        return min_num, f"{min_name}\n\t{name}"


def read_file(data_fp: IO) -> Tuple[float, str, float, str, float, str, float]:
    '''read a file and determine the max and min score and max no. of episodes and the average score'''
    max_score = 0
    max_score_name = 0
    max_episodes = 0
    max_episodes_name = 0
    min_score = 100000000
    min_score_name = 100000000
    total = 0
    count = 0
    for line in data_fp:
        title = line[0:100]
        title = title.strip()
        score = line[100:105]
        episodes = line[105:110]
        if not ("N/A" in score):
            score = float(score)
            max_score, max_score_name = find_max(score, title, max_score, max_score_name)
            min_score, min_score_name = find_min(score, title, min_score, min_score_name)
            total += score
            count += 1
        if not ("N/A" in episodes):
            episodes = float(episodes)
            max_episodes, max_episodes_name = find_max(episodes, title, max_episodes, max_episodes_name)
    return max_score, max_score_name, max_episodes, max_episodes_name, min_score, min_score_name, round((total/count), 2)


def search_anime(data_fp: IO, anime_name: str) -> Tuple[int, str]:
    '''search for an anime and return all matching anime'''
    output = ""
    count = 0
    for line in data_fp:
        title = line[0:100]
        release_season = line[110:122]
        if anime_name in title:
            count += 1
            output += f"\n\t{title}{release_season}"
    return count, output



def main():
    
    BANNER = "\nAnime-Planet.com Records" \
             "\nAnime data gathered in 2022"
    
    MENU ="Options" + \
          "\n\t1) Get max/min stats" + \
          "\n\t2) Search for an anime" + \
          "\n\t3) Stop the program!" + \
          "\n\tEnter option: "
    print(BANNER)
    while True:
        option = input(MENU)
        if option == "1":
            fp = open_file()
            max_score, max_score_name, max_episodes, max_episodes_name, min_score, min_score_name, avg_score = read_file(fp)
            print(f"\n\nAnime with the highest score of {max_score}:")
            print(max_score_name)
            print(f"\n\nAnime with the highest episode count of {max_episodes:,.0f}:")
            print(max_episodes_name)
            print(f"\n\nAnime with the lowest score of {min_score:.2f}:")
            print(min_score_name)
            print(f"\n\nAverage score for animes in file is {avg_score}")
            fp.close()
        elif option == "2":
            fp = open_file()
            anime_name = input("\nEnter anime name: ")
            count, output = search_anime(fp, anime_name)
            if count == 0:
                print(f"\nNo anime with '{anime_name}' was found!")
                continue
            print(f"\nThere are {count} anime titles with '{anime_name}'")
            print(output)
            fp.close()
        elif option == "3":
            print("\nThank you using this program!")
            break
        else:
            print("\nInvalid menu option!!! Please try again!")
    

# These two lines allow this program to be imported into other code
# such as our function tests code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.
#DO NOT CHANGE THESE 2 lines  
if __name__ == "__main__":
    main()
