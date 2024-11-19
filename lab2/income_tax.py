# Author: Ashton Tully
"""This calculates the income tax of employees"""

# Main method that calls other methods to compute tax
def main():
    """Allows for calculation of employee income""" 
    # variables for emp income
    employee_one_income = 38000
    employee_two_income = 96000
    # gets tax for employees
    employee_one_tax = compute_tax(employee_one_income)
    employee_two_tax = compute_tax(employee_two_income)
    # Prints necessary income and tax
    print_results(employee_one_income, employee_one_tax,
                  employee_two_income, employee_two_tax)
# Computes the tax for each income bracket
def compute_tax(income):
    """if income is less than 40000, then this if gets executed"""
    if income <= 40000:
        year_one_tax = income * .015
        year_two_tax = income * .0045
        year_three_tax = income * .0003
    # else if income is less than 80000, then this if gets executed
    elif income <= 80000:
        year_one_tax = income * .016
        year_two_tax = income * .0045
        year_three_tax = income * .0005
    # else if income is less than 105000, then this if gets executed
    elif income <= 105000:
        year_one_tax = income * .018
        year_two_tax = income * .0049
        year_three_tax = income * .0005
    # else if income is less than 205000, then this if gets executed
    elif income <= 250000:
        year_one_tax = income * .021
        year_two_tax = income * .0049
        year_three_tax = income * .011
    # adds the sum of all total taxes and returns it
    total = year_one_tax + year_two_tax + year_three_tax
    return total
# Prints the income and tax of both employees
def print_results(emp_one_income, emp_one_tax, emp_two_income, emp_two_tax):
    """Prints employee two income and tax"""
    print("Computing the tax for employee #1:")
    print("Net income: " + str(round(emp_one_income,1)))
    print("Total tax: " + str(round(emp_one_tax,1)))
    print()
    # Prints employee two income and tax
    print("Computing the tax for employee #2:")
    print("Net income: " + str(round(emp_two_income,1)))
    print("Total tax: " + str(round(emp_two_tax,1)))

# Using the variable __name__
if __name__ == "__main__":
    main()
