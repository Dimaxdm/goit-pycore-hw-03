from datetime import datetime, timedelta
from re import search, sub 
from random import sample


# global varialble
CURRENT_DATE: datetime = datetime.today().date()
DAYS_UPFRONT_OFFSET: int = 7 # in function related to Exercise 4


# helper function to parse date for Exercises 1 and 4
def parse_date(str_date: str, separator: str = ".") -> datetime:
    error_message_expected_format: str = f"Очікуваний формат \"РРРР{separator}ММ{separator}ДД\""
    # If missing parameter of the function >>> raise ValueError
    if not str_date:
        raise ValueError(f"Відсутній обов'язковий параметер функції! {error_message_expected_format}")
    
    date: str = str(str_date).strip()   # Remove spaces 
    pattern: str = r"(\d{4})[-./](\d{1,2})[-./](\d{1,2})"
    replacement: str = r"\1-\2-\3"
    match = search(pattern, date)
    
    # patter is not matching >>> raise ValueError
    if not match:
        raise ValueError(f"Не вірно зазначений параметер функції - \"{str_date}\"! {error_message_expected_format}")
        
        # return date of datetime object >>> "YYYY-mm-dd"
    try:
        return datetime.strptime(
            sub(pattern, replacement, date), 
            "%Y-%m-%d"
        ).date()
    except:
        raise ValueError(f"Не вірно зазначений параметер функції - \"{str_date}\"! {error_message_expected_format}")

# ======================= Exercise 1 ============================================
def get_days_from_today(date: str) -> int:
    parsed_date: datetime = parse_date(date, separator = "-") # using helper function
    return (CURRENT_DATE - parsed_date).days
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
    result: str = sub(r"\D", "", phone_number)

    if not result.startswith("38"):
        return "+38" + result

    return "+" + result
# ===============================================================================


# ======================= Exercise 4 ============================================
def get_offset_date_if_weekend(date: str) -> str:
    parsed_date: datetime = parse_date(date)
    # week [0 - Monday .. 6 - Sunday] 
    weekday : int = parsed_date.weekday()
    if weekday > 4:
        return datetime.strftime(parsed_date + timedelta(days = DAYS_UPFRONT_OFFSET - weekday), "%Y.%m.%d")
    
    return date


# Exercise 4
def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    days_in_year: int = 365 
    congratulation_list: list = []

    leap_year_offset: int = (
        datetime(year = CURRENT_DATE.year, month = 12, day = 31) - 
        datetime(year = CURRENT_DATE.year - 1, month = 12, day = 31)
    ).days - days_in_year

    for user in users:
        upcoming_birthday: str = f"{CURRENT_DATE.year}" + user["birthday"][4:]
        # use the function from Exercise 1 (can handle "YYYY-mm-dd" or "YYYY.mm.dd" date formats)
        days_difference: int = get_days_from_today(upcoming_birthday)
        congratulation_date: str = ""
        
        # if days_difference is between 0 and -7 then date considered as upcomming congratulation date
        if 0 >= days_difference >= -DAYS_UPFRONT_OFFSET:
            congratulation_date = get_offset_date_if_weekend(upcoming_birthday)
        
        # if days_difference is between 358 and 365 (or 359 and 366 in a leap year) then user HB is in next 7 days of next year
        if days_difference >= days_in_year + leap_year_offset - DAYS_UPFRONT_OFFSET:
            congratulation_date = get_offset_date_if_weekend(f"{CURRENT_DATE.year + 1}" + user["birthday"][4:])
        
        # 
        if congratulation_date != "":
            congratulation_list.append(
                {"name" : user["name"], "congratulation_date" : congratulation_date}
            )
    
    return congratulation_list
# ===============================================================================