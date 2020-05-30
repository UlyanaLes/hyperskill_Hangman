def check_email(string):
    if ' ' in string:
        return False
    if '@' not in string or string.count('@') > 1:
        return False
    if string.rfind('@') > string.rfind('.'):
        return False
    if string.rfind('@') + 1 == string.rfind('.'):
        return False
    return True


# print(check_email('good.email@example.com'))
