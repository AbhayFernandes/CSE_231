#######################################################
# Computer Project #9
#
# Algorithm
#  1. Prompt user for file name
#  2. Open file
#  3. Read file
#  4. Create a set of all words in file
#  5. Create a dictionary of all possible letter combinations
#  6. Prompt user for prefix
#  7. Find all words that complete the prefix
#  8. Print all words that complete the prefix
#  9. Repeat steps 6-8 until user enters "#"
# 10. Exit program
#######################################################

import string
from typing import Set, Dict, Tuple, TextIO


def open_file():
    """
    Prompts user for file name and opens file
    """
    while True:
        try:
            fp = open(input("\nInput a file name: "), "r")
            return fp
        except FileNotFoundError:
            print("\n[Error]: no such file")


def read_file(fp: TextIO) -> Set[str]:
    """
    Reads file and creates a set of all words in file
    """
    out_set = set()
    for line in fp:
        # get all words in a line
        words = line.split()
        for word in words:
            # remove punctuation and make lowercase
            word = word.strip(string.punctuation).lower()
            # add word to set if it is not empty and is alphabetical
            if word.isalpha() and len(word) >= 2:
                out_set.add(word)
    return out_set


def fill_completions(words: Set[str]) -> Dict[Tuple[int, str], Set[str]]:
    """
    Creates a dictionary of all possible letter combinations
    and their respective positions in a word.
    """
    word_list = list(words)
    letter_dic = {}
    # create a dictionary of all possible letter combinations
    for word in word_list:
        # get a for loop that has both the index and the letter
        for letter in enumerate(word):
            # if tuple (index, position) not in letter_dic:
            if (letter[0], letter[1]) not in letter_dic:
                # add tuple (index, position) to letter_dic
                letter_dic[(letter[0], letter[1])] = set()
    # add words to letter_dic
    for position in letter_dic:
        for word in word_list:
            # if letter at position[0] in word is equal to position[1]:
            # add word to letter_dic[position]
            # try except to prevent index error
            try:
                if word[position[0]] == position[1]:
                    letter_dic[position].add(word)
            except IndexError:
                pass
    return letter_dic


def find_completions(prefix: str, word_dic: Dict[Tuple[int, str], Set[str]]) \
    -> Set[str]:
    """
    Finds all words that complete the prefix
    """
    out_set = list()
    # get a for loop that has both the index and the letter
    for position in enumerate(prefix):
        # if tuple (index, position) in word_dic:
        # add word_dic[(index, position)] to out_set
        if (position[0], position[1]) in word_dic:
            out_set.append(word_dic[(position[0], position[1])])
        else:
            return set()
    # find intersection of all sets in out_set, by creating an iterator
    # and passing it to set.intersection
    return set.intersection(*out_set)


def set_to_string(in_set: Set[str]) -> str:
    """
    Converts a set to a string
    """
    out_str = ""
    in_list = list(in_set)
    in_list.sort()
    for word in in_list:
        out_str += word + ", "
    # return the created string sans the last two characters
    return out_str[:-2]


def main():
    file = open_file()
    word_dic = fill_completions(read_file(file))
    while True:
        prefix = input("\nEnter a prefix (# to quit): ")
        if prefix == "#":
            print("\nBye")
            break
        completions = find_completions(prefix, word_dic)
        if len(completions) == 0:
            print("\nThere are no completions.")
        else:
            print(
                f"\nThe words that completes {prefix}",
                "are: {set_to_string(completions)}"
            )


if __name__ == "__main__":
    main()
