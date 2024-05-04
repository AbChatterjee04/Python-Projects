def main():
    print("calculate your easy monthly installment or emi ")
    print("")

    principal = float(input("Enter the principle amount: "))
    air = float(input("Enter the annual interest rate: "))
    years = int(input("Enter number of years: "))

    monthly_interest_rest = air/ 1200
    no_of_months = years * 12
    monthly_payment = principal * monthly_interest_rest / (1 - (1 + monthly_interest_rest) ** (-no_of_months))


    print("The monthly payment for this loan is : %.2f"  % monthly_payment)    

main()
