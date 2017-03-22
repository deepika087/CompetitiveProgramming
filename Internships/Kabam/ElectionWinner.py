def  electionWinner(votes):
    result = dict()
    for item in votes:
        if (result.get(item, -1) == - 1):
            result[item] = 1
        else:
            result[item] = result[item] + 1


    result=sorted(result.items(), key=lambda x: x[1], reverse=True)
    #print type(result)
    max_votes = result[0][1]
    if (len(result) <= 1):
        return result[0][0]
    else:
        name_result=[]
        for item in result:
            if (item[1] == max_votes):
                name_result.append(item[0])

        name_result = sorted(name_result, reverse=True)
        return name_result[0]
    #print max_votes


if __name__=="__main__":

    print electionWinner(["A","A", "C", "B", "B", ""]);