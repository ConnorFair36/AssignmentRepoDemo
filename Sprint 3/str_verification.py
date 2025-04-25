import re
def valid_name(name: str) -> bool:
    """Verifies the name is in the form: 'First Last'."""
    return bool(re.match("[A-Z][a-z]* [A-Z][a-z]*", name))

def valid_password(password: str) -> bool:
    """Ensures the password is al least 8 characters long and contains a number and 
    a special character."""
    if len(password) < 8:
        return False
    return bool(re.match(".*[0-9].*", password)) and bool(re.match(".*[()+!_\-@#$%\^&*].*", password))

def valid_phone_num(phone_num: str) -> bool:
    """Ensures the phone number is in one of these forms: xxxxxxxxxx, (xxx)xxx-xxxx"""
    if len(phone_num) == 13:
        phone_num = phone_num.replace("(", "").replace(")", "").replace("-", "")
    return bool(re.match("[0-9]{10}", phone_num))

def valid_email(email: str) -> bool:
    """Ensures the email is in the form: alphanum@alphanum.alphanum"""
    return bool(re.match("\w+@\w+\.\w+", email))

def valid_conditions(conditions: str) -> bool:
    """Ensures the coditions contain only alphanumeric characters"""
    return bool(re.match("\w+", conditions))

def valid_severity(severity: str) -> bool:
    """Ensures the severity is between 1 and 5 inclusive"""
    return bool(re.match("[1-5]", severity)) and len(severity) == 1

def valid_time(time: str) -> bool:
    """Ensures the time is in the form 0≤hour≤23:0≤min≤59 """
    if bool(re.match("[0-9]{1,2}:[0-9]{2}", time)):
        hour, minute = time.split(":")
        return 3 <= len(time) <= 5 and 0 <= int(hour) <= 23 and 0 <= int(minute) <= 59
    return False

def valid_birthday(birthday: str) -> bool:
    """Ensures the birthday is in the form: MM-DD-YYYY."""
    if bool(re.match("[0-1][0-9]-[0-3][0-9]-[0-2][0-9]{3}", birthday)) and len(birthday) == 10:
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
