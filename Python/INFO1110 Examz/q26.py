def blackjack(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    if a not in range(1,14):
        raise ValueError("Incorrect card number!")
    elif b not in range(1,14):
        raise ValueError("Incorrect card number!")
    elif c not in range(1,14):
        raise ValueError("Incorrect card number!")
    else:
        pass
    sum = a + b + c
    if sum == 21:
        return True
    else:
        return False

print(blackjack(10, 10, 1))
print(blackjack(13, 1, 7))