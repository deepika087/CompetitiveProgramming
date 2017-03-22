


if __name__ == "__main__":

    N = int(raw_input(''))
    names = list()

    #codes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73, 79,83,89,97, 101]
    anagrams = dict()
    #print len(codes)
    for i in range(N):
        name = raw_input('')
        name = name.lower()
        name1 = "".join(sorted(name))

        if (anagrams.get(name1, -1) == -1):
            anagrams[name1] = 1
        else:
            anagrams[name1] = anagrams.get(name1) + 1

    count = 0
    for i, items in anagrams.items():
        if (items > 1):
            count = count + items

    #print anagrams
    print count
