

def itemSafeToAdd(maps, item):
    for line in maps:
        if (item == line[0] and int(line[1]) > 0):
            return False
    return True #only occurs on the right side

if __name__ == "__main__":
    N = int(raw_input(''))

    maps = []
    for i in range(N):
        line = raw_input('')
        line = line.split()
        maps.append(line)

    evaluate = raw_input('')
    evaluate = evaluate.split()

    stack = []
    assigned = False
    for item in evaluate:
        if (itemSafeToAdd(maps, item)):
            stack.append(item)
        else:
            # item occurs on left side line before integer it means it has prerequisities
            if (len(stack) == 0): #first element in array
                print "BOOM!"
                assigned = True
                break;
            else:
                #Check if prerequisite is present in stack
                prereq = []
                for _ in maps:
                    if (_[0] == item):
                        prereq = _[2:]
                        break;
                for p in prereq:
                    if ( p in stack):
                        continue
                    else:
                        print "BOOM!"
                        assigned = True
                        break;
                stack.append(item)

    if (not assigned):
        print "SAFE!"
