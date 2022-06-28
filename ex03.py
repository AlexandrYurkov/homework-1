def zeros(n):
    result = 0
    while n > 0:
        n /= 5
        result += (int(n))
    return result
