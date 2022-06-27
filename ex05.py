global max_value
global max_count

def check_sum(numbers):
    result = 1
    for i in range(len(numbers)):
        result *= numbers[i]
    print(result)
    return result


def copy_list(primesL):
    numbers = []
    for i in range(len(primesL)):
        numbers.append(primesL[i])
    return numbers


def loop(numbers, limit, primesL, i):
    global max_count, max_value
    sum = check_sum(numbers)
    while limit >= sum:
        if limit >= max_value and sum > max_value:
            max_value = sum
        max_count += 1
        numbers.append(primesL[i])
        sum = check_sum(numbers)


def count_find_num(primesL, limit):
    max_value = 0
    max_count = 0
    result = []
    numbers = copy_list(primesL)
    print(numbers)
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

        print(numbers)
        if i >= 1 and sum >= limit:
            print("_____________")
            numbers.pop(-1)
            sum = check_sum(numbers)
            while limit >= sum:
                i = 0
                if limit >= max_value and sum >= max_value:
                    max_value = sum
                max_count += 1
                numbers.append(primesL[i])
                sum = check_sum(numbers)
                print(numbers)


        numbers = copy_list(primesL)

    # if max_count > 0 and max_value > 0:
    result.append(max_count)
    result.append(max_value)
    return result


def test():

    primesL = [2, 3]
    limit = 200
    print(count_find_num(primesL, limit))
    #[13, 192]
    # primesL = [2, 5]
    # limit = 200
    # print(count_find_num(primesL, limit) == [8, 200])
    #
    primesL = [2, 3, 5]
    limit = 500
    print(count_find_num(primesL, limit))
    #== [12, 480]
    primesL = [2, 3, 5]
    limit = 1000
    print(count_find_num(primesL, limit))
    # == [19, 960]
    # primesL = [2, 3, 47]
    # limit = 200
    # print(count_find_num(primesL, limit) == [])



if __name__ == '__main__':
    test()