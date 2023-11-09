# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # line = print("------------------------------")#30
    # valid = print("Valid Entry")
    # restart = print("Resting program")

    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = int(input("Set your desired savings account balance: "))
    if savings_balance > 0:
        print("------------------------------")#30
        print("Valid Entry")
    else:
        print("Resting program")
        main()

    savings_interest = float(input("Set your desired savings interest rate: "))
    if savings_interest > 0:
        print("------------------------------")#30
        print("Valid Entry")
    else:
        print("Resting program")
        main()

    savings_maturity = int(input("Set your length of time in months: "))
    if savings_maturity > 0:
        print("------------------------------")#30
        print("Valid Entry")
    else:
        print("Resting program")
        main()

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"The interest earned on you savings account is: {interest_earned:.2f}\n Savings balance: {updated_savings_balance:.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = int(input("Set your desired CD account balance: "))
    if cd_balance > 0:
        print("------------------------------")#30
        print("Valid Entry")
    else:
        print("Resting program")
        main()

    cd_interest = float(input("Set your desired CD interest rate: "))
    if cd_interest > 0:
        print("------------------------------")#30
        print("Valid Entry")
    else:
        print("Resting program")
        main()

    cd_maturity = int(input("Set your length of time in months: "))
    if cd_maturity > 0:
        print("------------------------------")#30
        print("Valid Entry")
    else:
        print("Resting program")
        main()

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"The interest earned on you savings account is: {interest_earned:.2f}\nSavings balance: {updated_cd_balance:.2f}")

if __name__ == "__main__":
    # Call the main function.
    main()