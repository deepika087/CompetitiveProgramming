__author__ = 'deepika'

# Complete the function below.
# The team person selects best person from m in front and m in back.
#
def teamFormation(score, team, m):

    if team == len(score):
        return sum(score)

    teamSize = 0
    result = []

    while teamSize != team:
        if len(score) > m:
           mLeft = m
           mRight = len(score) - m
           part1 = score[0:mLeft]
           part2 = score[mRight:]

           while mLeft < mRight:
               max_part1 = max(part1)
               max_part1_index = part1.index(max_part1)

               max_part2 = max(part2)
               max_part2_index = len(score) - m + part2.index(max_part2)

               if max_part1 > max_part2:
                   result.append(max_part1)
                   score.pop(max_part1_index)
               elif max_part2 > max_part1:
                   result.append(max_part2)
                   score.pop(max_part2_index)
               else: #If equal
                   if max_part1_index < max_part2_index:
                       score.pop(max_part1_index)
                   else:
                       score.pop(max_part2_index)
               teamSize = teamSize + 1
               if teamSize == team:
                   break
        if len(score) == m:
            score = sorted(score)
            result += score[0:team - teamSize]
            teamSize = team
            break
        else:
            if teamSize < team:
                score = sorted(score, reverse=True)
                result += score[0:team - teamSize]
                teamSize = team
    #print result
    return sum(result)



def teamFormation(score, team, m):

    if team == len(score):
        return sum(score)

    teamSize = 0
    result = []
    while teamSize != team:
        if len(score) > m:
           part1 = score[0:m]
           part2 = score[len(score) - m:]

           max_part1 = max(part1)
           max_part1_index = part1.index(max_part1)

           max_part2 = max(part2)
           max_part2_index = len(score) - m + part2.index(max_part2)

           if max_part1 > max_part2:
               result.append(max_part1)
               score.pop(max_part1_index)
           elif max_part2 > max_part1:
               result.append(max_part2)
               score.pop(max_part2_index)
           else: #If equal
               if max_part1_index < max_part2_index:
                   score.pop(max_part1_index)
               else:
                   score.pop(max_part2_index)
           teamSize = teamSize + 1
           if teamSize == team:
               break
        if len(score) == m:
            score = sorted(score)
            result += score[0:team - teamSize]
            teamSize = team
            break
        else:
            if teamSize < team:
                score = sorted(score, reverse=True)
                result += score[0:team - teamSize]
                teamSize = team
    #print result
    return sum(result)

#print teamFormation([17, 12, 10, 2, 7, 2, 11, 20, 8], 3, 4)
print teamFormation([6, 18, 8, 14, 10, 12, 18, 9], 8, 3)