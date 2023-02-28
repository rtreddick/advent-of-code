from pyprojroot import here


def insertSum(maxSums, currentSum):
    
    if currentSum > maxSums[0]:
        maxSums[0] = currentSum
        for idx in range(len(maxSums) - 1):
            if maxSums[idx] > maxSums[idx + 1]:
                maxSums[idx], maxSums[idx + 1] = maxSums[idx+1], maxSums[idx]


def findMostCalories(path, nTop):
    maxSums = [0] * nTop

    with open(path, 'r') as lines:
        currentSum = 0

        for line in lines:
            if line == '\n':
                insertSum(maxSums, currentSum)
                currentSum = 0
            else:
                currentSum += int(line)
    
    return sum(maxSums)
            

if __name__ == "__main__":

    path = f"{here('./01/calories.txt')}"
    sumTopN = findMostCalories(path, 3)
    print(sumTopN)