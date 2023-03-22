
import string
import os
from operator import itemgetter


def add_word( word_map, word ):
    word = word.lower()
    if word == "":
        return
    # YOUR COMMENT
    if word not in word_map:
        word_map[ word ] = 0

    # YOUR COMMENT
    word_map[ word ] += 1


def build_map( in_file, word_map ):

    for line in in_file:

        # YOUR COMMENT
        word_list = line.split()

        for word in word_list:

            # YOUR COMMENT
            word = word.strip().strip(string.punctuation)
            add_word( word_map, word )
        

def display_map( word_map ):

    word_list = list()

    # YOUR COMMENT
    for word, count in word_map.items():
        word_list.append( (word, count) )

    # sort alphabetically first
    word_list = sorted( word_list, key=itemgetter(0) )
    # YOUR COMMENT
    freq_list = sorted( word_list, key=itemgetter(1), reverse=True )

    print( "\n{:15s}{:5s}".format( "Word", "Count" ) )
    print( "-"*20 )
    for item in freq_list:
        print( "{:15s}{:>5d}".format( item[0], item[1] ) )


def open_file(file_path):
    file_path = os.path.join( os.getcwd(), file_path)
    try:
        in_file = open( file_path, "r" )
        print() #keep it for testing purposes in Coding Rooms
    except IOError:
        print( "\n*** unable to open file ***\n" )
        in_file = None

    return in_file


word_map = dict()
file_path = input("Enter file name: ")
in_file = open_file(file_path)

if in_file != None:

    build_map( in_file, word_map )
    display_map( word_map )
    in_file.close()


