def list_res(word):
    result = []
    for c in word:
        result = c
    return result


def bananas(word):
    s = list(word)
    result = set()
    shab = list("banana")
    i = 0
    j = 0
    print(s)
    for i in range(len(s)):
        if s[i] == shab[j]:
            # print(s[i])
            # print(s[i], shab[j])
            i += 1
            while i < len(s) and j < len(shab) and s[i] == shab[j]:
                s[i] = '-'
                i += 1
            j += 1
    return s


def test():
    print(bananas("bbbananna"))


if __name__ == '__main__':
    test()

#
# assert bananas("banann") == set()
# assert bananas("banana") == {"banana"}
# assert bananas("bbananana") == {"b-an--ana",
#                                 "-banana--",
#                                 "-b--anana",
#                                 "b-a--nana",
#                                 "-banan--a",
#                                 "b-ana--na",
#                                 "b---anana",
#                                 "-bana--na",
#                                 "-ba--nana",
#                                 "b-anan--a",
#                                 "-ban--ana",
#                                 "b-anana--"}
# assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
# assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}
