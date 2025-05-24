monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

savings = monthly_income - monthly_expenses
print(f"Your monthly savings are: ${savings}")

projected_annual_savings = savings * 12 +(savings * 12 * 0.05)  # Adding 5% monthly interest on savings
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings}")
# This code calculates monthly savings and projects annual savings with interest.
# It prompts the user for their monthly income and expenses, calculates the savings,
# and then projects the annual savings by multiplying the monthly savings by 12 and adding 5% interest.
# The results are printed in a formatted string.
# The code is simple and demonstrates basic arithmetic operations in Python.
# It serves as a basic example of how to perform financial calculations in Python.