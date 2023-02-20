''' Insert heading comments here.'''
from typing import Tuple

def open_file():
    ''' open file and return file pointer'''
    while True:
        file_path = input("\nEnter filename: ")
        try:
            fp = open(file_path, "r", enconding="utf-8")
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


def read_file(data_fp) -> Tuple[float, str, float, str, float, str, float]:
    '''read a file and determine the max and min score and max no. of episodes and the average score'''
    max_score = 0
    max_score_name = 0
    max_episodes = 0
    max_episodes_name = 0
    min_score = 0
    min_score_name = 0
    total = 0
    count = 0
    for line in data_fp:
        title = line[0:100]
        score = line[100:105]
        episodes = line[105:110]
        if not ("N/A" in score):
            score = float(score)
            max_score, max_score_name = find_max(score, title, max_score, max_score_name)
            min_score, min_name = find_min(score, title, min_score, min_score_name)
            total += score
            count += 1
        if not ("N/A" in episodes):
            episodes = float(episodes)
            max_episodes, max_episodes_name = find_max(episodes, title, max_episodes, max_episodes_name)
    return max_score, max_score_name, max_episodes, max_episodes_name, min_score, min_score_name, (total/count)


def search_anime(data_fp, anime_name):
    '''Insert docstring here.'''
    pass  # insert your code here


def main():
    
    BANNER = "\nAnime-Planet.com Records" \
             "\nAnime data gathered in 2022"
    
    MENU ="Options" + \
          "\n\t1) Get max/min stats" + \
          "\n\t2) Search for an anime" + \
          "\n\t3) Stop the program!" + \
          "\n\tEnter option: "
    
    print(BANNER)
    

# These two lines allow this program to be imported into other code
# such as our function tests code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.
#DO NOT CHANGE THESE 2 lines  
if __name__ == "__main__":
    main()
