from datetime import datetime, date, timedelta
from typing import Dict

def get_celebration_day_from_birthday(birthday: date) -> date:
    """
    Returns celebration day from birthday by shifting it away from weekend:
    Saturday to Monday,
    Sunday to Monday
    
    Parameters:
        birthday (date): Birthday date on current year or next
    """
    weekday = birthday.isoweekday()
    shift = 0 if weekday not in [6, 7] else (8 - weekday)
    return birthday + timedelta(days=shift)

def get_next_celebration_day(user: Dict[str, str]) -> date:
    """
    Returns celebration day for user on current year or next.
    
    Parameters:
        user (dict): User data as dictionary, e.g.: {"name": "John Doe", "birthday": "1985.01.23"}
    """
    today = date.today()
    dob = datetime.strptime(user["birthday"], "%Y.%m.%d").date() # Date of birth
    birthday = date(today.year, dob.month, dob.day)
    # Get celebration date before comparison with today:
    # If birthday is on Saturday, and today is Sunday - we still can congratulate on Monday
    celebration = get_celebration_day_from_birthday(birthday)
    if celebration >= today:
        return celebration
    else:
        # If celebration date passed - congratulation comes next year
        birthday = date(today.year + 1, dob.month, dob.day)
        celebration = get_celebration_day_from_birthday(birthday)
        return celebration

def get_upcoming_birthdays(users):
    today = date.today()
    results = []
    for user in users:
        day = get_next_celebration_day(user)
        if (day - today).days <= 7: # Inclusive, if today is Friday, Friday is included
            dto = {
                "name": user["name"],
                "congratulation_date": datetime.strftime(day, "%Y.%m.%d")
            }
            results.append(dto)
    return results

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.11.27"},
    {"name": "Joe Friday", "birthday": "1925.10.03"},
    {"name": "Joe Saturday", "birthday": "1925.10.04"},
    {"name": "Joe Sunday", "birthday": "1925.10.05"},
    {"name": "Joe Monday", "birthday": "1925.10.06"},
    {"name": "Joe Nextweek", "birthday": "1925.10.10"},
    {"name": "Joe NotYet", "birthday": "1925.10.11"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print(upcoming_birthdays)
