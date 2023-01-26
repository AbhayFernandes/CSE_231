########################################################
# Computer Project #1

# Algorithm:
#     prompt user for floating point value representing distance
#     input the float
#     store within various variables the following conversions:
#         - meters
#         - feet
#         - miles 
#         - furlongs
#         - time in minutes to walk
#     output these conversions (rounded to 3 decimal points).
########################################################

ROD_TO_METERS = 5.0292
ROD_TO_FEET = 16.5
ROD_TO_MILES = 0.003125
ROD_TO_FURLONGS = 0.025
ROD_TO_MINUTES = 0.06048399291

rods = input("Input rods: ")
rod_float = float(rods)
print("\nYou input", round(rod_float, 3), "rods.\n")
# Output the appropriate conversions by multiplying
# the input by the conversion factor.
print("Conversions")
print("Meters:", round(rod_float * ROD_TO_METERS, 3))
print("Feet:", round(rod_float * ROD_TO_FEET, 3))
print("Miles:", round(rod_float * ROD_TO_MILES, 3))
print("Furlongs:", round(rod_float * ROD_TO_FURLONGS, 3))
print("Minutes to walk", round(rod_float, 3), \
    "rods:", round(rod_float * ROD_TO_MINUTES, 3))
