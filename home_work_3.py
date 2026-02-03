from datetime import datetime, timedelta
from re import search, sub 
from random import sample


# ======================= Exercise 1 ============================================
# ---------- Additional functions for Exercise 1 --------------------------------
# return message in case of incorrect format
def incorrect_format_return(variable: str) -> None:
    return f"\"{variable}\" not following correct pattern \"YYYY-MM-DD\"!"


# validation of the correct format of the 
def validation_date_format(date: str) -> datetime | bool: # Used in Exercise 1
    # trim space(s)
    date: str = str(date).strip()
    pattern: str = r"(\d{4})[-./](\d{1,2})[-./](\d{1,2})"
    replacement: str = r"\1-\2-\3"
    match = search(pattern, date)
    
    if match:
        # return correct pattern "YYYY-mm-dd"
        return sub(pattern, replacement, date)
    else:
        # return False in case wrong pattern
        return False
# ------------------------------------------------------------------------------

# Exercise 1
def get_days_from_today(date: str) -> int:
    # 1.1 input in format 'YYYY-MM-DD'
    # 1.2 convert 
    validated_date: str = validation_date_format(date)
    if not validated_date:
        return incorrect_format_return(date)

    try:
        converted_date: datetime = datetime.strptime(validated_date, "%Y-%m-%d")
    except: 
        return incorrect_format_return(date)
    
    current_date: datetime = datetime.today()
    # 1.5 return number of days s integer between prompted and current date
    return (current_date - converted_date).days
# ===============================================================================


# ======================= Exercise 2 ============================================
def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int | None]:
    under_bound: int = 1
    upper_bound: int = 1_000

    # if min < 1 || max > 1000 || quantity > (max - min)
    if (min < under_bound or max > upper_bound) or (quantity > (max - min)):
        return []
    
    list_result: list = sorted(sample(range(min, max), quantity))
    return list_result
# ===============================================================================


# ======================= Exercise 3 ============================================
# Exercise 3
def normalize_phone(phone_number: str) -> str:
    # # solution without regular expressions 
    # numberic_part_of_phone_number: str = "".join([num for num in phone_number if num.isnumeric()])
    # if numberic_part_of_phone_number[:2] == "38":
    #     return "+" + numberic_part_of_phone_number
    # 
    # return "+38" + numberic_part_of_phone_number

    # regular expressions solution
    # exclude any non-digit character
    result: str = sub("\D", "", phone_number)

    if not result.startswith("38"):
        return "+38" + result

    return "+" + result
# ===============================================================================


# ======================= Exercise 4 ============================================
# ---------- Additional functions for Exercise 4 --------------------------------
# if user BD within 7 days or less than return congratulation date
# if not satisfied required then return False 
def validation_of_upcoming_birthday(user_birthday_date: str) -> datetime | bool:
    user_birthday: datetime = datetime.strptime(user_birthday_date, "%Y.%m.%d")
    current_date: datetime = datetime.today().date()
    user_birthday_this_year: datetime = user_birthday.replace(year = current_date.year).date()

    if 0 <= (user_birthday_this_year - current_date).days <= 7:
        # weekday [0 - Monday .. 6 = Sunday]
        weekday : int = user_birthday_this_year.weekday()
        if weekday > 4: # 
            return user_birthday_this_year + timedelta(days = 7 - weekday)

        return user_birthday_this_year
    
    return False
# ------------------------------------------------------------------------------

# Exercise 4
def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    congratulation_list: list = []
    
    for user in users:
        upcoming_birthday = validation_of_upcoming_birthday(user["birthday"])
        if upcoming_birthday:
            congratulation_list.append(
                {"name" : user["name"], "congratulation_date" : upcoming_birthday.strftime("%Y.%m.%d")}
            )
    
    return congratulation_list
# ===============================================================================
