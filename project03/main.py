NUMBER_OF_PAYMENTS = 360    # 30-year fixed rate mortgage, 30 years * 12 monthly payments
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
APR_2023 = 0.0668*100

def get_monthly_payment(P, I, N):
    """Return the monthly payment for a mortgage loan."""
    I = (I/100) / 12
    return P * (I * (1 + I) ** N) / ((1 + I) ** N - 1)

def get_principal(M, I, N):
    """Return the maximum principal that can be purchased with a given monthly payment."""
    I = (I/100) / 12
    num = M*((1+I)**N - 1)
    denom = I*(1+I)**N
    return num / denom

def get_monthly_taxes(home_price, tax_rate):
    """Return the monthly property tax for a home."""
    return home_price * (tax_rate / 12)

def print_amortization_table(monthly_payment, APR, principal):
    balance = principal
    print(f"\n{'Month':^7}|{'Interest':^12}|{'Principal':^13}|{'Balance':^14}")
    print("================================================")
    for i in range(1, NUMBER_OF_PAYMENTS + 1):
        interest = balance * ((APR/100) / 12)
        principal = monthly_payment - interest
        print(f"{i:^7d}| ${interest:>9.2f} | ${principal:>10.2f} | ${balance:>11.2f}")
        balance -= principal

''' WRITE YOUR CODE USING THE CONSTANT VALUES ABOVE '''
print("\nMORTGAGE PLANNING CALCULATOR\n============================ ")
print("\nEnter a value for each of the following items or type 'NA' if unknown ")
done = False
while not done:
    location = input("\nWhere is the house you are considering (Seattle, San Francisco, Austin, East Lansing)? ")
    sq_feet = input("\nWhat is the maximum square footage you are considering? ")
    monthly_payment = input("\nWhat is the maximum monthly payment you can afford? ")
    down_payment = input("\nHow much money can you put down as a down payment? ")
    apr = input("\nWhat is the current annual percentage rate? ")

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
        print("\nUnknown location. Using national averages for price per square foot and tax rate.")

    if sq_feet == "NA" and monthly_payment == "NA":
        print("\nYou must either supply a desired square footage or a maximum monthly payment. Please try again.")
        continue  

    if down_payment == "NA":
        down_payment = 0
    else:
        down_payment = float(down_payment)
    
    if apr == "NA":
        apr = APR_2023
    else:
        apr = float(apr)

    if sq_feet != "NA":
        sq_feet = float(sq_feet)
        principal = (sq_feet * price_per_sq_foot) - down_payment
        calculated_monthly_payment = get_monthly_payment(principal, apr, NUMBER_OF_PAYMENTS) 
        monthly_taxes = get_monthly_taxes((sq_feet * price_per_sq_foot), tax)

        print(f"\n\nIn {location}, an average {sq_feet:.0f} sq. foot house would cost ${(sq_feet * price_per_sq_foot):.0f}.")
        print(f"A 30-year fixed rate mortgage with a down payment of ${down_payment:.0f} at {apr:.1f}% APR results")
        print(f"\tin an expected monthly payment of ${monthly_taxes:.2f} (taxes) + ${calculated_monthly_payment:.2f} (mortgage payment) = ${(monthly_taxes + calculated_monthly_payment):.2f}")

        if monthly_payment != "NA":     
            monthly_payment = float(monthly_payment)
            if (monthly_taxes + calculated_monthly_payment) > monthly_payment:
                print(f"Based on your maximum monthly payment of ${monthly_payment:.2f} you cannot afford this house.")
            elif (monthly_taxes + calculated_monthly_payment) <= monthly_payment:
                print(f"Based on your maximum monthly payment of ${monthly_payment:.2f} you can afford this house.")
        else:
            pass

        table = input("\nWould you like to print the monthly payment schedule (Y or N)? ").lower()
        if table == "y":
            print_amortization_table(calculated_monthly_payment, apr, principal)
        else:
            pass

    else:
        sq_feet = (get_principal(float(monthly_payment), apr, NUMBER_OF_PAYMENTS) + down_payment) / price_per_sq_foot
        principal = (sq_feet * price_per_sq_foot) - down_payment
        calculated_monthly_payment = get_monthly_payment(principal, apr, NUMBER_OF_PAYMENTS) 
        monthly_taxes = get_monthly_taxes((sq_feet * price_per_sq_foot), tax)
        print(f"\n\nIn {location}, a maximum monthly payment of ${float(monthly_payment):.2f} allows the purchase of a house of {sq_feet:.0f} sq. feet for ${(sq_feet * price_per_sq_foot):.0f}")
        print(f"\t assuming a 30-year fixed rate mortgage with a ${down_payment:.0f} down payment at {apr:.1f}% APR.")
    
    done_str = input("\nWould you like to make another attempt (Y or N)? ").lower()
    if done_str != 'y':
        break