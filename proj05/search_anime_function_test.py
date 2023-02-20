from main import search_anime
import os

# Non-Empty Case (Single Title)

# open the test file
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, "anime_tiny.txt")
fp = open(filename, "r", encoding="utf-8")

# Instructor values
search_str = "Saint Seiya"
inst_count = 1
inst_anime_titles = "\n\tSaint Seiya: Knights of the Zodiac                                                                  fall 1986   "

# Call the read_file function
stu_count, stu_anime_titles = search_anime(fp, search_str)


# Run the assertion tests
print(f"inst_count: {inst_count} stu_count: {stu_count}")
print(f"inst_anime_titles: {inst_anime_titles} \nstu_anime_titles: {stu_anime_titles}")
assert inst_count == stu_count
assert inst_anime_titles == stu_anime_titles

fp.close()

# Non-Empty Case (Multi Title)

# open the test file
fp = open(filename, "r", encoding="utf-8")

# Instructor values
search_str = "Dragon Ball"
inst_count = 2
inst_anime_titles = "\n\tDragon Ball Z: Bojack Unbound                                                                       summer 1993 " + \
                	"\n\tDragon Ball Super: Broly                                                                            fall 2018   "

# Call the read_file function
stu_count, stu_anime_titles = search_anime(fp, search_str)

# Run the assertion tests
print(f"inst_count: {inst_count} stu_count: {stu_count}")
print(f"inst_anime_titles: {inst_anime_titles} stu_anime_titles: {stu_anime_titles}")
assert inst_count == stu_count
assert inst_anime_titles == stu_anime_titles

fp.close()
