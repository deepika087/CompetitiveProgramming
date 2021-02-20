__author__ = 'deepika'

def findMutationDistance(start, end, bank):

    def isviable(current, string):
        diff = 0
        for i in range(len(current)):
            if current[i] != string[i]:
                diff = diff + 1
        return diff == 1

    queue = []
    visited = set()
    queue.append([start, start , 0])
    visited.add(start)
    results = [start]
    while queue:
        current, previous, steps = queue.pop()

        if current == end:
            print results
            return steps

        for string in bank:
            if string not in visited and isviable(current, string) and string != previous:
                results.append(string)

                visited.add(string)
                queue.append([string, current, steps + 1])

assert  findMutationDistance("AACCGGTT", "AACCGGTA", ["AACCGGTA"]) == 1
assert  findMutationDistance("AAAAACCC", "AACCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"]) == 3