import re

def normalize_phone(phone_number: str) -> str:
    """
    Normalizes phone number: accept phone numbers in international format,
    and UA phone numbers in internation and local format, "+" is optional if starts with UA prefix "380"

    Parameters:
        phone_number (str): Phone number to normalize

    Returns:
        str: Normalized phone number in international starting with "+" followed by digits only
    """
    has_plus_prefix = re.search(r"^\D*\+", phone_number)          # If plus present at start: international number, add plus before numbers
    has_380_prefix = re.search(r"^\D*3\D*8\D*0", phone_number)    # If 380 present at start: UA number, add plus before numbers
    numbers = re.sub(r"[\D+]", "", phone_number)                  # Cleanup non-digits          
    prefix = "+" if has_plus_prefix or has_380_prefix else "+38"  # If unrecognized: add UA prefix without zero
    return prefix + numbers

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "3805012+34567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)888+9900",
    "+38 (050)-111-22-22",
    "+3 80 50 111 22 11   ",
    "(+1) (555) 1234+5678"
]

for phone_number in raw_numbers:
    print(normalize_phone(phone_number))
