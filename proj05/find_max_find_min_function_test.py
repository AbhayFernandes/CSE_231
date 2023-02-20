from proj05 import find_max, find_min

###### find_max function test ################################################

from proj05 import find_max

# Case 1: Initial max_value change

# Instructor values
inst_max_episode = 1.0
inst_max_episode_name = "\n\tChamebou Kuukijuu no Maki"

line_episode, line_name = 1.0, "Chamebou Kuukijuu no Maki"
stu_max_episode, stu_max_episode_name = 0, ""

print("Inputs max value and name:",stu_max_episode,stu_max_episode_name)
print("Inputs value and name:",line_episode,line_name)
print("Instructor max value and name:",inst_max_episode,inst_max_episode_name)
stu_max_episode, stu_max_episode_name = find_max(line_episode, line_name, stu_max_episode, stu_max_episode_name)
print("Student max value and name:",stu_max_episode,stu_max_episode_name)
assert inst_max_episode == stu_max_episode
assert inst_max_episode_name == stu_max_episode_name

# Case 2: Multiple max_names with same max_value
print(20*'-')
# Instructor values
inst_max_score = 5.07
inst_max_score_name = "\n\tTiny Chibisuke's Big Adventure" +\
                        "\n\tShinsetsu Kachikachi Yama"

line_score, line_name = 5.07, "Shinsetsu Kachikachi Yama"
stu_max_score, stu_max_score_name = 5.07, "\n\tTiny Chibisuke's Big Adventure"
print("Inputs max value and name:",stu_max_score,stu_max_score_name)
print("Inputs value and name:",line_score,line_name)
print("Instructor max value and name:",inst_max_score,inst_max_score_name)
stu_max_score, stu_max_score_name = find_max(line_score, line_name, stu_max_score, stu_max_score_name)
print("Student max value and name:",stu_max_score,stu_max_score_name)

assert inst_max_score == stu_max_score
assert inst_max_score_name == stu_max_score_name

# ##############################################################################

###### find_min function test ################################################


# Case 1: Initial max_value change

# Instructor values 
inst_min_episode = 1.0
inst_min_episode_name = "\n\tChamebou Kuukijuu no Maki" + \
                        "\n\tBurglars of Baghdad Castle" + \
                        "\n\tThe Stolen Lump" + \
                        "\n\tHarvest Festival" + \
                        "\n\tFushigi na Taiko" + \
                        "\n\tThe World of Hans Christian Andersen"


line_episode, line_name = 1.0, "The World of Hans Christian Andersen"

stu_min_episode = 1.0 
stu_min_episode_name = "\n\tChamebou Kuukijuu no Maki" + \
                        "\n\tBurglars of Baghdad Castle" + \
                        "\n\tThe Stolen Lump" + \
                        "\n\tHarvest Festival" + \
                        "\n\tFushigi na Taiko"

stu_min_episode, stu_min_episode_name = find_min(line_episode, line_name, stu_min_episode, stu_min_episode_name)

assert inst_min_episode == stu_min_episode
assert inst_min_episode_name == stu_min_episode_name

# Case 2: Min value change

# Instructor values
inst_min_score = 3.1
inst_min_score_name = "\n\tSuper Child"

line_score, line_name = 3.1, "Super Child"
stu_min_score, stu_min_score_name = 4.05, "\n\tNinja Fireball in Edo"        
stu_min_score, stu_min_score_name = find_min(line_score, line_name, stu_min_score, stu_min_score_name)
        
assert inst_min_score == stu_min_score
assert inst_min_score_name == stu_min_score_name



##############################################################################