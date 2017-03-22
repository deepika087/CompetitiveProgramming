
def getWater(heights, distances, i, j):
    #if (heights[i] < heights[j]):


    Height = max(heights[i+1:]) if (heights[i] > heights[j]) else heights[i]
    Distance = sum(distances[i:j])
    NumberOfPillars = j - i - 1

    crudeSum=Height * (Distance + NumberOfPillars*1)
    sumT = 0
    for pillar in range(i+1, j):
        sumT = sumT + heights[pillar] * 1
    return crudeSum - sumT

def getMaxLakeVolume(heights, distances):

    i = 0
    maxVol = -1
    while ( i < len(heights) and i + 1 < len(heights)):
        start = i
        end = start + 1

        while(end < len(heights) and heights[end] < heights[start]):
            #if (end + 1 < len(heights)):
                end = end + 1
        if(end == len(heights)):
            end = end - 1
        print " Calling for start = ", start, " and end = ", end
        vol = getWater(heights, distances, start, end)
        #print " for start = ", start, " and end = ", end, " received vol = ", vol
        if (vol > maxVol):
            maxVol = vol
        i = end
    return maxVol

if __name__=="__main__":
    heights = [3, 10, 4, 5, 7]
    distances = [1, 2, 3, 4]

    heights = [4, 7, 4, 9, 6]
    distances = [3, 9, 6, 2]

    print getMaxLakeVolume(heights, distances) #Expected 108

