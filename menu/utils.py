import re

def get_input(prompt, retry=True, target_type=str):
    """
    Get and Return user inputs after validating them
    """
    assert callable(target_type)

    try:
        user_input = input(prompt)  # if Ctrl+C -> raise KeyboardInterrupt
        user_input = target_type(user_input)
    except KeyboardInterrupt:
        print("\nForce Exit...")
        exit(0)
    except Exception as err:
        if retry:
            print("Invalid input, try again")
            return get_input(prompt, retry, target_type)
        else:
            raise TypeError("Invalid input, try again") from err  # NewException -> err
    return user_input

def yes_no_return_function(value):
    if value == '1':
        return "YES"
    elif value == '2':
        return "NO"
    else:
        raise Exception
def logging(content):
    with open("logging.log", 'a') as f:
        f.write(content + '\n')

class UserLoginSignal(Exception):
    pass

def username_validation(username):
    reg = "^[A-Za-z][A-Za-z0-9_]{7,29}$"
    pat = re.compile(reg)
    if re.fullmatch(pat, username):
        return username
    else:
        raise Exception

def password_validation(password):
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    pat = re.compile(reg)
    if re.fullmatch(pat, password):
        return password
    else:
        raise Exception

def email_validation(email):
    reg = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
    pat = re.compile(reg)
    if re.fullmatch(pat, email):
        return email
    else:
        raise Exception

def phone_validation(phone):
    reg = "^(\\+\\d{1,3}( )?)?((\\(\\d{1,3}\\))|\\d{1,3})[- .]?\\d{3,4}[- .]?\\d{4}$"
    pat = re.compile(reg)
    if re.fullmatch(pat, phone):
        return phone
    else:
        raise Exception