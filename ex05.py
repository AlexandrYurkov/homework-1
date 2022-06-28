def check_sum(numbers):
    result = 1
    for i in range(len(numbers)):
        result *= numbers[i]
    return result


def copy_list(primesL):
    numbers = []
    for i in range(len(primesL)):
        numbers.append(primesL[i])
    return numbers


def loop(primesL, limit):
    max_count = 0
    max_value = 0
    result = []
    numbers = copy_list(primesL)
    for i in range(len(primesL)):
        sum = check_sum(numbers)
        if i == 0 and sum > limit:
            break
        while limit >= sum:
            if limit >= max_value and sum > max_value:
                max_value = sum
            max_count += 1
            numbers.append(primesL[i])
            sum = check_sum(numbers)

        if max_count > 0 and max_value > 0:
            result.append(max_count)
            result.append(max_value)

        return result


def count_find_num(primesL, limit):
    value = 0
    count = (len(primesL) + 1) * - 1
    result = []
    tmp = copy_list(primesL)
    len_list = len(primesL) - 1
    i = 0
    j = 1

    if check_sum(primesL) > limit:
        return result

    while i < len(primesL):
        if 0 < len_list == i:
            tmp.append(primesL[j])
            len_list -= 1
            j += 1
            i = 0
        else:
            check = loop(tmp, limit)
            i += 1
            if check[1] > value:
                value = check[1]
            count += check[0]

    result.append(count)
    result.append(value)
    return result
