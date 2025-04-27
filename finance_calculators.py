import math

invest_input_1 = "INVESTMENT"
invest_input_2 = "investment"
invest_input_3 = "Investment"

bond_input_1 = "BOND"
bond_input_2 = "bond"   
bond_input_3 = "Bond"

def investment(amount, rate, years, interest_type):
    """Calculate simple or compound interest."""
    rate /= 100  # Convert percentage to decimal
    if interest_type.lower() == "simple":
        return amount * (1 + rate * years)
    elif interest_type.lower() == "compound":
        return amount * (1 + rate) ** years
    else:
        return "Invalid interest type. Choose 'simple' or 'compound'."

def bond(amount, rate, months):
    """Calculate monthly bond repayment."""
    rate = (rate / 100) / 12  # Convert annual rate to monthly
    return (rate * amount) / (1 - (1 + rate) ** -months)

# Below is the input from the user
print("Investment - to calculate the amount of interest you'll earn on your investment.")
print("Bond - to calculate the amount you'll have to pay on a home loan.")
print("Choose either 'Investment' or 'Bond' from the menu above to proceed: ")

user_input = input("Enter your choice: ")

if (user_input == invest_input_1) or (user_input == invest_input_2) or (user_input == invest_input_3):
    invest_amnt = float(input("Enter the amount you want to invest: "))
    invest_interest = float(input("Enter the interest rate (in %): "))
    years = int(input("Enter the number of years: "))
    interest_type = input("Enter 'simple' or 'compound' interest: ")
    
    result = investment(invest_amnt, invest_interest, years, interest_type)
    print(f"Future investment value: {result:.2f}" if isinstance(result, float) else result)

elif (user_input == bond_input_1) or (user_input == bond_input_2) or (user_input == bond_input_3):
    home_value = float(input("Enter the house value (loan amount): "))
    home_interest = float(input("Enter the interest rate (in %): "))
    months = int(input("Enter the number of months for repayment: "))

    result = bond(home_value, home_interest, months)
    print(f"Your monthly bond repayment: {result:.2f}")

else:
    print("Invalid choice. Please enter investment or bond.")


