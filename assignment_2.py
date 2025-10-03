from typing import List

import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> List[int]:
    """
    Generates lottery ticket with 'quantity' unique random numbers in range between 'min' and 'max' (inclusive)

    Parameters:
        min (int): Minimal number
        max (int): Maximum number
        quantity (int): Quantity of numbers in ticket

    Returns:
        List[int]: Sorted list which contains unique random numbers
    """
    if min > max:
        print(f"Can't generate numbers in range [{min}, {max}]")
        return []
              
    max_quantity = max - min + 1
    if quantity > max_quantity:
        print(f"Can't generate {quantity} unique numbers, maximum quantity is {max_quantity}")
        return []
        
    numbers = set()
    while len(numbers) < quantity:
        number = random.randint(min, max)
        numbers.add(number)

    return sorted(numbers)

print(get_numbers_ticket(10, 10, 1)) # [10]
print(get_numbers_ticket(1, 10, 10)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(get_numbers_ticket(11, 10, 1)) # [], Can't generate numbers in range [11, 10]
print(get_numbers_ticket(10, 10, 2)) # [], Can't generate 2 unique numbers, maximum quantity is 1
print(get_numbers_ticket(1, 50, 10)) # some random ticket
