import re
def valid_name(name: str) -> bool:
    """Verifies the name is in the form: 'First Last'."""
    return bool(re.match("[A-Z][a-z]* [A-Z][a-z]*"), name)

def valid_password(password: str) -> bool:
    """Ensures the password is al least 8 characters long and contains a number and 
    a special character."""
    if len(password) < 8:
        return False
    return bool(re.match(".*[0-9].*"), password) and bool(re.match(".*[()+_\-@#$%\^&*].*", password))

def valid_phone_num(phone_num: str) -> bool:
    """Ensures the phone number is in one of these forms: xxxxxxxxxx, (xxx)xxx-xxxx"""
    if len(phone_num) == 13:
        phone_num = phone_num.replace("(", "").replace(")", "").replace("-", "")
    return bool(re.match("[0-9]{10}", phone_num))

def valid_email(email: str) -> bool:
    """Ensures the email is in the form: alphanum@alphanum.alphanum"""
    return bool(re.match("\w+@\w+\.\w+", email))

def valid_institution_name(inst_name: str) -> bool:
    """Ensures the institution name contains only alphanumeric characters"""
    return bool(re.match("\w+", inst_name))

def valid_conditions(conditions: str) -> bool:
    """Ensures the coditions contain only alphanumeric characters"""
    return bool(re.match("\w+", conditions))

def valid_severity(severity: str) -> bool:
    """Ensures the severity is between 1 and 5 inclusive"""
    return bool(re.match("[1-5]", severity))

def valid_time(time: str) -> bool:
    """Ensures the time is either: 0≤hour≤23:0≤min≤59 or (AM|PM)1≤hour≤12:0≤min≤59"""
    if len(time) == 5:
        hour = time[:2]
        minute = time[3:]
        if bool(re.match("[0-2][0-9]", hour)) and bool(re.match("[0-5][0-9]", minute)):
            hour = int(hour)
            minute = int(minute)
            return 0 <= hour <= 23 and 0 <= minute <= 59
        return False
    elif len(time) == 7:
        am_or_pm = time[:2]
        hour = time[2:4]
        minute = time[5:]
    if bool(re.match("[0-2][0-9]", hour)) and bool(re.match("[0-5][0-9]", minute)):
        hour = int(hour)
        minute = int(minute)
        return 1 <= hour <= 12 and 0 <= minute <= 59 and am_or_pm in ["AM", "am", "PM", "pm"]
    return False

def valid_birthday(birthday: str) -> bool:
    """Ensures the birthday is in the form: MM-DD-YYYY."""
    if bool(re.match("[0-1][0-9]-[0-3][0-9]-[0-2][0-9]{3}", birthday)):
        month, day, year = birthday.split("-")
        return 1 <= int(month) <= 12 and 1 <= int(day) <= 31
    return False

def valid_sex(sex: str) -> bool:
    """Ensures sex is either: M, F, male, female"""
    sex = sex.upper()
    return sex in ["M", "F", "MALE", "FEMALE"]

def valid_insurance(insurance: str) -> bool:
    """Ensures the coditions contain only alphanumeric characters"""
    return bool(re.match("\w+", insurance))
