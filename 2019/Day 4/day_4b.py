def day_4b():
    lower = 128392
    upper = 643281
    valid_passwords = 0
    for i in range (lower, upper + 1):
        if has_exactly_two(str(i)) and same_or_increasing(str(i)):
            valid_passwords +=1
    print(valid_passwords)


def has_exactly_two(nr):
    count = 1
    for i in range(1, len(nr)):
        if nr[i] == nr[i - 1]:
            count +=1
        else:
            if count == 2:
                return True
            count = 1
    return count == 2


def same_or_increasing(nr):
    for i in range(0, len(nr) - 1):
        if nr[i] > nr[i + 1]:
            return False
    return True


day_4b()
