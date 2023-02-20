from main import read_file, find_max, find_min
import os
# open the test file
filename = os.path.join(os.path.dirname(__file__), "anime_tiny.txt")
fp = open(filename, "r", encoding="utf-8")

# Instructor values
inst_max_score = 8.54
inst_max_score_name = "\n\tThe Promised Neverland"
inst_max_episodes = 1006.0
inst_max_episode_name = "\n\tSekai Monoshiri Ryoko"
inst_min_score = 2.76
inst_min_score_name = "\n\tClap Vocalism"
inst_avg_score = 6.66

# Call the read_file function
stu_max_score, stu_max_score_name, stu_max_episodes, stu_max_episode_name, \
            stu_min_score, stu_min_score_name, stu_avg_score = read_file(fp)

# Run the assertion tests
print(f"inst_max_score: {inst_max_score} \nstu_max_score: {stu_max_score}")
print(f"inst_max_score_name: {inst_max_score_name} \nstu_max_score_name: {stu_max_score_name}")
print(f"inst_max_episodes: {inst_max_episodes} \nstu_max_episodes: {stu_max_episodes}")
print(f"inst_max_episode_name: {inst_max_episode_name} \nstu_max_episode_name: {stu_max_episode_name}")
print(f"inst_min_score: {inst_min_score} \nstu_min_score: {stu_min_score}")
print(f"inst_min_score_name: {inst_min_score_name} \nstu_min_score_name: {stu_min_score_name}")
print(f"inst_avg_score: {inst_avg_score} \nstu_avg_score: {stu_avg_score}")
assert inst_max_score == stu_max_score
assert inst_max_score_name == stu_max_score_name
assert inst_max_episodes == stu_max_episodes
assert inst_max_episode_name == stu_max_episode_name
assert inst_min_score == stu_min_score
assert inst_min_score_name == stu_min_score_name
assert inst_avg_score == stu_avg_score