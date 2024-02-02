def slif(s, s1, s2):
    if s1 == "==":
        if s == s2:
            return True
        else:
            return False
    elif s1 == "!=":
        if s != s2:
            return True
        else:
            return False
    elif s1 == ">":
        if s > s2:
            return True
        else:
            return False
    elif s1 == "<":
        if s < s2:
            return True
        else:
            return False
    elif s1 == ">=":
        if s >= s2:
            return True
        else:
            return False
    elif s1 == "<=":
        if s <= s2:
            return True
        else:
            return False

def slelse(last_code):
    if slif(last_code.split()[1], last_code.split()[2], last_code.split()[3]) == False:
        return True