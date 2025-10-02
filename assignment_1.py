from datetime import datetime

def get_days_from_today(date: str) -> int | None:
    """
    Calculates amount of days to today

    Parameters:
        date (str): Starting date

    Returns:
        Optional[int]: Amount of days to today,
                       0 if date is today,
                       Negative if date is later,
                       None if date format is invalid
    """
    try:
        parsed_date = datetime.strptime(date, "%Y-%m-%d")
        now = datetime.today()
        delta = now - parsed_date
        return delta.days
    except ValueError:
        print(f"Invalid argument: '{date}' does not match format 'YYYY-MM-DD'")
        return None

# Today: 2025-10-03

print(get_days_from_today("2025-09"))    # Output: None
print(get_days_from_today("2025-09-03")) # Output: 30
print(get_days_from_today("2025-10-02")) # Output:  1
print(get_days_from_today("2025-10-03")) # Output:  0
print(get_days_from_today("2025-10-04")) # Output: -1
print(get_days_from_today("2025-10-05")) # Output: -2
