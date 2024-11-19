# Author: Ashton Tully 
# Dr.Goodman
# CSE 174 J
# 11/16/2024
"""
Lab 12
"""
def read_file(filename: str):
    """
    Reads file and creates list of customers.
    
    Args:
        filename (str): Name of file.

    Returns:
        list: A list that contains a customer and an ID.
    
    """
    customer_list=[]
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) == 2:
                    customer_list.append([parts[0], parts[1]])
    except FileNotFoundError:
        print("Error %s not found." % (filename))
    return customer_list

def linear_search(customer_list: list, key: list):
    """
    Performs a linear search for a key in the customer list.
    
    Args:
        customer_list (list): A list of customers.
        key (list): A list with the customer name and ID to search for.

    Returns:
        int: The index of the key if found, or -1 if not found.
    """
    comparisons = 0
    for index, customer in enumerate(customer_list):
        comparisons += 1
        if customer == key:
            print("Linear Search: the key is found after %d comparisons." 
                  % (comparisons))
            return index
    print("Linear Search: the key is found after %d comparisons." 
        % (comparisons))
    return -1


def binary_search(customer_list: list, key: list):
    """
    Performs a binary search for a key in the customer list.
    
    Args:
        customer_list (list): A list of customers.
        key (list): A list with the customer name and ID to search for.

    Returns:
        int: The index of the key if found, or -1 if not found.
    """
    comparisons = 0
    left, right = 0, len(customer_list) - 1
    while left <= right:
        comparisons += 1
        mid = (left + right) // 2
        if customer_list[mid][1] == key[1]:
            print("Binary Search: the key is found after %d comparisons." 
                  % (comparisons))
            return mid
        elif customer_list[mid][1] < key[1]:
            left = mid + 1
        else:
            right = mid - 1
    print("Binary Search: the key is found after %d comparisons." 
        % (comparisons))
    return -1

def print_list(customer_list: list):
    """
    Prints formated lists.

    Args:
        customer_list (list): List of customers and IDs.
    """
    index = linear_search(customer_list, ["Delilah", "4350600189"])
    print("The customer ['Delilah', '4350600189'] is located at index: %d.\n" 
          % index)
    index = binary_search(customer_list, ["Delilah", "4350600189"])
    print("The customer ['Delilah', '4350600189'] is located at index: %d.\n" 
          % index)

    index = linear_search(customer_list, ["Zola", "2074980639"])
    print("The customer ['Zola', '2074980639'] is located at index: %d.\n" 
          % index)
    index = binary_search(customer_list, ["Zola", "2074980639"])
    print("The customer ['Zola', '2074980639'] is located at index: %d.\n" 
          % index)

    index = linear_search(customer_list, ["Reinaldo", "9988586038"])
    print("The customer ['Reinaldo', '9988586038'] is located at index: %d.\n"
          % index)
    index = binary_search(customer_list, ["Reinaldo", "9988586038"])
    print("The customer ['Reinaldo', '9988586038'] is located at index: %d.\n"
          % index)

    index = linear_search(customer_list, ["CSE174", "1111111111"])
    print("The customer ['CSE174', '1111111111'] is located at index: %d.\n" 
          % index)
    index = binary_search(customer_list, ["CSE174", "1111111111"])
    print("The customer ['CSE174', '1111111111'] is located at index: %d." 
          % index)
    
def main():
    # Reads file and prints list
    customer_list =  read_file("customer_list.txt")
    print_list(customer_list)

if __name__ == "__main__":
    main()