from typing import List

import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> List[int]:
    """
    Generates lottery ticket with 'quantity' unique random numbers in range between 'min' and 'max' (inclusive)

    Parameters:
        min (int): Minimal number, >= 1
        max (int): Maximum number, <= 1000
        quantity (int): Quantity of numbers in ticket, between min and max

    Returns:
        List[int]: Sorted list which contains unique random numbers
    """
    MIN = 1
    MAX = 1000

    if min < MIN:
        print(f"Min is less than minimum: {min} < {MIN}")
        return []
    
    if max > MAX:
        print(f"Max is greater than maximum: {max} > {MAX}")
        return []
    
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

print(get_numbers_ticket(10, 10, 1))  # [10]
print(get_numbers_ticket(1, 10, 10))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(get_numbers_ticket(11, 10, 1))  # [], Can't generate numbers in range [11, 10]
print(get_numbers_ticket(10, 10, 2))  # [], Can't generate 2 unique numbers, maximum quantity is 1
print(get_numbers_ticket(0, 10, 1))   # [], Min is less than minimum: 0 < 1
print(get_numbers_ticket(1, 1001, 1)) # [], Max is greater than maximum: 1001 > 1000
print(get_numbers_ticket(1, 50, 10))  # some random ticket
