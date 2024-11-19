# Author: Ashton Tully
# Dr. Goodman
# CSE 174 J
# 11/02/2024
# Copyright: 2024 Ashton Tully
"""Lab 10"""

def read_file(filename: str) -> list:
    """Reads file and returns list of orders.
    
    Args:
        filename (str): The name of the file to read.
        
    Returns:
        list: List or orders
    """
    try:
        # Opens the file and reads line by line
        with open(filename, 'r') as file:
            orders = []
            for line in file:
                # Split each line into a list of four items and add to orders
                orders.append(line.strip().split())
            return orders
    except FileNotFoundError:
        # If the file is not found, return an empty list
        return []
def get_order_profits(x: list) -> list:
    """Calculates profits from list of orders.
    
    Args:
        x (list): List containing orders.
        
    Returns:
        list: List of profits calculated from order amounts and prices.
    """
    profits = []
    for order in x:
        # Extract amount and price from each order
        amount = int(order[2])
        price = float(order[3])
        # Calculate profit
        profit = amount * price
        profits.append(profit)
    return profits

def display(x: list):
    """Displays profits.
    
    Args:
        x (list): List of profits.
    """
    count = 1
    for profit in x:
        print("Order #%d profit is $%.2f." % (count, profit))
        count += 1

    print("Average profit is $%.2f." % get_average_profit(x))
    print("Total profit is $%.2f." % get_total_profit(x))
    
def get_average_profit(x: list) -> float:
    """Calculates average profit.
    
    Args:
        x (list): List of profits.
        
    Returns:
        float: Average profit.
    """
    total = 0
    for num in x:
        total += num
    return total / len(x)
def get_total_profit(x: list) -> float:
    """Calculates total profit.
    
    Args:
        x (list): List of profits.
        
    Returns:
        float: Total profit.
    """
    total = 0
    for num in x:
        total += num
    return total
def main():
    print("Enter file name: ", end='')
    filename = input()
    orders = read_file(filename)
    profits = get_order_profits(orders)
    display(profits)

if __name__ == '__main__':
    main()
