import itertools


def list_res(word):
    result = []
    for c in word:
        result = c
    return result


def check_test(words, word):
    flag = True
    for i in range(len(words)):
        if (words[i] == '-' or words[i] == word[i]) and i < len(words):
            i += 1
        else:
            flag = False
    return flag


def bananas(word):
    s = list(word)
    result = set()
    shab = list("banana")
    j = 0
    for i in range(len(s)):
        if j < len(shab) and s[i] == shab[j]:
            i += 1
            while i < len(s) and j < len(shab) and s[i] == shab[j]:
                s[i] = '-'
                i += 1
            j += 1
        elif i < len(s):
            s[i] = '-'
    for i in itertools.permutations(s):
        tmp = "".join("".join(i).split("-"))
        if tmp == "banana":
            s.append("".join(i))
    for res in s:
        tmp = "".join("".join(res).split("-"))
        if check_test(res, word) and tmp == "banana":
            result.add(res)
    return result
