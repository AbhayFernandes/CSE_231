###########################################################
#  Computer Project #2
#
#  Algorithm
#    prompt user for all the variables required
#        begin by doing basic computations \
#        nescessary for all branches.
#        branch off based on the code the user inputted.
#            complete the computations required for only that branch
#        output the same generic format with the calculated values
#        loop back to prompting the user based on the input of the user
#    display closing message should the user choose to exit
###########################################################

import math
MILEAGE_COST = 0.25
BUDGET_DAILY_COST = 40
DAILY_COST = 60
DAILY_MILEAGE_ALLOWANCE = 100
WEEKLY_BASE_COST = 190
WEEKLY_LOW_MILEAGE_ALLOWANCE = 900
WEEKLY_LOW_MILEAGE_COST = 100
WEEKLY_HIGH_MILEAGE_ALLOWANCE = 1500
WEEKLY_HIGH_MILEAGE_COST = 200


print("\nWelcome to Horizons car rentals. \
\n\nAt the prompts, please enter the following: \
\n\tCustomer's classification code (a character: BD, D, W) \
\n\tNumber of days the vehicle was rented (int)\
\n\tOdometer reading at the start of the rental period (int)\
\n\tOdometer reading at the end of the rental period (int)")

done = input("\nWould you like to continue (A/B)? ")
while done != 'B':
    code = input("\nCustomer code (BD, D, W): ")
    if code == 'BD' or code == 'D' or code == 'W':
        days = input("\nNumber of days: ")
        odometer_start = input("\nOdometer reading at the start: ")
        odometer_end = input("\nOdometer reading at the end:   ")
        days = int(days)
        cost = 0
        num_miles = ((int(odometer_end) - int(odometer_start))/10)

        # Handle if the odometer reading is less than the starting reading
        if num_miles < 0:
            num_miles += 100000

        if code == 'BD':
            cost = BUDGET_DAILY_COST * days + MILEAGE_COST * num_miles

        elif code == 'D':
            cost = DAILY_COST * days
            if num_miles >= days * DAILY_MILEAGE_ALLOWANCE:
                cost += MILEAGE_COST * \
                (num_miles - (days * DAILY_MILEAGE_ALLOWANCE))

        elif code == 'W':
            weeks = days / 7
            ceil_weeks = math.ceil(weeks)
            cost = WEEKLY_BASE_COST * ceil_weeks
            if num_miles < (WEEKLY_LOW_MILEAGE_ALLOWANCE * weeks):
                pass

            elif (WEEKLY_LOW_MILEAGE_ALLOWANCE * weeks) < num_miles and \
            num_miles < (WEEKLY_HIGH_MILEAGE_ALLOWANCE * weeks):
                cost += WEEKLY_LOW_MILEAGE_COST * ceil_weeks

            elif num_miles > (WEEKLY_HIGH_MILEAGE_ALLOWANCE * weeks):
                cost += WEEKLY_HIGH_MILEAGE_COST * ceil_weeks
                cost += (num_miles - \
                (WEEKLY_HIGH_MILEAGE_ALLOWANCE * ceil_weeks)) * MILEAGE_COST


        print("\n\nCustomer summary:")
        print("\tclassification code:", code)
        print("\trental period (days):", days)
        print("\todometer reading at start:", int(odometer_start))
        print("\todometer reading at end:  ", int(odometer_end))
        print("\tnumber of miles driven: ", round(num_miles, 1))
        print("\tamount due: $", float(round(cost, 2)))
    else:
        print("\n\t*** Invalid customer code. Try again. ***")
        continue

    done = input("\nWould you like to continue (A/B)? ")

print("\nThank you for your loyalty.")
