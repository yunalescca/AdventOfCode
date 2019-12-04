def day_4a():
    lower = 128392
    upper = 643281
    valid_passwords = 0
    for i in range (lower, upper + 1):
        if has_two_adjacent(str(i)) and same_or_increasing(str(i)):
            valid_passwords +=1
    print(valid_passwords)


def has_two_adjacent(nr):
    for i in range(0, len(nr) - 1):
        if nr[i] == nr[i + 1]:
            return True
    return False


def same_or_increasing(nr):
    for i in range(0, len(nr) - 1):
        if nr[i] > nr[i + 1]:
            return False
    return True


day_4a()