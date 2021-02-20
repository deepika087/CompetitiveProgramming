__author__ = 'deepika'


def minimumTime(numOfSubFiles, files):
    if (numOfSubFiles == 1):
        return files[0]
    if (numOfSubFiles == 2):
        return  files[0] + file[1]

    files = sorted(files)
    totalTime = files[0] + files[1]
    cummulative = totalTime

    i = 2
    while (i < numOfSubFiles):
        totalTime += files[i]
        cummulative += totalTime
        i = i + 1

    return cummulative


print(minimumTime(4, [4, 8, 6, 12]))
print(minimumTime(4, [20, 4, 8, 2]))
