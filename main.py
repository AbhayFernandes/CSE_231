###########################################################
#  Computer Project #3
#
#  Algorithm
#    prompt user for all the variables required
#        begin by doing basic computations \
#        nescessary for all branches.
#        branch off based on the code the user inputted.
#            complete the computations required for only that branch
#        output the same generic format with the calculated values
#        output the amortization table should the user want it
#        loop back to prompting the user based on the input of the user
###########################################################


# CONSTANTS ---------------------------------------------------------------
NUMBER_OF_PAYMENTS = 360
SEATTLE_PROPERTY_TAX_RATE = 0.0092
SAN_FRANCISCO_PROPERTY_TAX_RATE = 0.0074
AUSTIN_PROPERTY_TAX_RATE = 0.0181
EAST_LANSING_PROPERTY_TAX_RATE = 0.0162
AVERAGE_NATIONAL_PROPERTY_TAX_RATE = 0.011
SEATTLE_PRICE_PER_SQ_FOOT = 499.0
SAN_FRANCISCO_PRICE_PER_SQ_FOOT = 1000.0
AUSTIN_PRICE_PER_SQ_FOOT = 349.0
EAST_LANSING_PRICE_PER_SQ_FOOT = 170.0
AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT = 244.0
APR_2023 = 0.0668 * 100

# FUNCTIONS ---------------------------------------------------------------
def get_monthly_payment(P, I, N):
    """Return the monthly payment for a mortgage loan.
    P = principal
    I = annual interest rate
    N = number of payments
    Returns the monthly payment for a mortgage loan. Produced with given
    Formula.
    """
    I = (I / 100) / 12
    return P * (I * (1 + I) ** N) / ((1 + I) ** N - 1)


def get_principal(M, I, N):
    """Return the maximum principal that can be 
    purchased with a given monthly payment.
    M = monthly payment
    I = annual interest rate
    N = number of payments
    Returns the maximum principal that can 
    be purchased with a given monthly payment.
    Essentially, this is the inverse of the get_monthly_payment function."""
    I = (I / 100) / 12
    num = M * ((1 + I) ** N - 1)
    denom = I * (1 + I) ** N
    return num / denom


def get_monthly_taxes(home_price, tax_rate):
    """Return the monthly property tax for a home.
    home_price = price of the home
    tax_rate = property tax rate
    Returns the monthly property tax for a home."""
    return home_price * (tax_rate / 12)


def print_amortization_table(monthly_payment, APR, principal):
    """Print an amortization table for a mortgage loan.
    monthly_payment = monthly payment
    APR = annual percentage rate
    principal = principal
    Prints an amortization table for a mortgage loan."""
    balance = principal
    print(f"\n{'Month':^7}|{'Interest':^12}|{'Principal':^13}|{'Balance':^14}")
    print("================================================")
    for i in range(1, NUMBER_OF_PAYMENTS + 1):
        interest = balance * ((APR / 100) / 12)
        principal = monthly_payment - interest
        print(f"{i:^7d}| ${interest:>9.2f} |",
        f"${principal:>10.2f} | ${balance:>11.2f}")
        balance -= principal


# MAIN --------------------------------------------------------------------
done = False
while not done:
    print("\nMORTGAGE PLANNING CALCULATOR\n============================ ")
    print("\nEnter a value for each of the "\
        "following items or type 'NA' if unknown ")
    # Get user input for all variables
    location = input(
        "\nWhere is the house you are considering "\
        "(Seattle, San Francisco, Austin, East Lansing)? "
    )
    sq_feet = input("\nWhat is the maximum square "\
        "footage you are considering? ")
    monthly_payment = input("\nWhat is the maximum monthly payment "\
        "you can afford? ")
    down_payment = input("\nHow much money can you put "\
        "down as a down payment? ")
    apr = input("\nWhat is the current annual percentage rate? ")


    # Set the tax rate and price per square foot based on location
    if location == "Seattle":
        tax = SEATTLE_PROPERTY_TAX_RATE
        price_per_sq_foot = SEATTLE_PRICE_PER_SQ_FOOT
    elif location == "San Francisco":
        tax = SAN_FRANCISCO_PROPERTY_TAX_RATE
        price_per_sq_foot = SAN_FRANCISCO_PRICE_PER_SQ_FOOT
    elif location == "Austin":
        tax = AUSTIN_PROPERTY_TAX_RATE
        price_per_sq_foot = AUSTIN_PRICE_PER_SQ_FOOT
    elif location == "East Lansing":
        tax = EAST_LANSING_PROPERTY_TAX_RATE
        price_per_sq_foot = EAST_LANSING_PRICE_PER_SQ_FOOT
    else:
        tax = AVERAGE_NATIONAL_PROPERTY_TAX_RATE
        price_per_sq_foot = AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT
        location = "the average U.S. housing market"
        print(
            "\nUnknown location. Using national averages "\
            "for price per square foot and tax rate."
        )

    # Handle invalid input of NA for all variables
    if sq_feet == "NA" and monthly_payment == "NA":
        print(
            "\nYou must either supply a desired square footage "\
            "or a maximum monthly payment. Please try again."
        )
        continue

    # Handle input of NA for down payment and APR
    if down_payment == "NA":
        down_payment = 0
    else:
        down_payment = float(down_payment)

    if apr == "NA":
        apr = APR_2023
    else:
        apr = float(apr)

    # Branch based on whether the user supplied a desired square footage
    if sq_feet != "NA":
        sq_feet = float(sq_feet)
        principal = (sq_feet * price_per_sq_foot) - down_payment
        calculated_monthly_payment = get_monthly_payment(
            principal, apr, NUMBER_OF_PAYMENTS
        )
        monthly_taxes = get_monthly_taxes((sq_feet * price_per_sq_foot), tax)

        print(
            f"\n\nIn {location}, an average {sq_feet:.0f} sq. foot house "\
            f"would cost ${(sq_feet * price_per_sq_foot):.0f}."
        )
        print(
            f"A 30-year fixed rate mortgage with a down payment of "\
            f"${down_payment:.0f} at {apr:.1f}% APR results"
        )
        print(
            f"\tin an expected monthly payment of ${monthly_taxes:.2f} "\
            f"(taxes) + ${calculated_monthly_payment:.2f} (mortgage payment) "\
            f"= ${(monthly_taxes + calculated_monthly_payment):.2f}"
        )

        #branch based on whether the user supplied a maximum monthly payment
        if monthly_payment != "NA":
            monthly_payment = float(monthly_payment)
            tot_monthly_payment = monthly_taxes + calculated_monthly_payment
            if (tot_monthly_payment) > monthly_payment:
                print(
                    f"Based on your maximum monthly payment of "\
                    f"${monthly_payment:.2f} you cannot afford this house."
                )
            elif (tot_monthly_payment) <= monthly_payment:
                print(
                    f"Based on your maximum monthly payment of "\
                    f"${monthly_payment:.2f} you can afford this house."
                )
        else:
            pass

        table = input(
            "\nWould you like to print the monthly payment schedule (Y or N)? "
        ).lower()
        if table == "y":
            print_amortization_table(calculated_monthly_payment, apr, principal)
        else:
            pass

    #branch whether the user supplied a maximum monthly payment
    else:
        #calculate the maximum square footage that can be purchased
        sq_feet = (
            get_principal(float(monthly_payment), apr, NUMBER_OF_PAYMENTS)
            + down_payment
        ) / price_per_sq_foot
        principal = (sq_feet * price_per_sq_foot) - down_payment
        calculated_monthly_payment = get_monthly_payment(
            principal, apr, NUMBER_OF_PAYMENTS
        )
        monthly_taxes = get_monthly_taxes((sq_feet * price_per_sq_foot), tax)
        print(
            f"\n\nIn {location}, a maximum monthly payment of "\
            f"${float(monthly_payment):.2f} allows the purchase "\
            f"of a house of {sq_feet:.0f} sq. feet for "\
            f"${(sq_feet * price_per_sq_foot):.0f}"
        )
        print(
            f"\t assuming a 30-year fixed rate mortgage with "\
            f"a ${down_payment:.0f} down payment at {apr:.1f}% APR."
        )
    # Ask the user if they want to make another attempt
    done_str = input("\nWould you like to make "\
        "another attempt (Y or N)? ").lower()
    if done_str != "y":
        break
