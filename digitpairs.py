from itertools import combinations

numberOfElements = int(input())
rawNumbers = str(input())
rawNumbersList = rawNumbers.split(' ')

def calculateBitScore(number):
    numberList = list(map(lambda x: int(x), list(number)))
    a = max(numberList) * 11
    b = min(numberList) * 7
    c = a + b
    if(len(str(c)) >= 3):
        return str(c)[1:]
    return str(c)

def calculateDigitPairs(bitScoreList):
    oddPairs = []
    evenPairs = []
    for i, value in enumerate(bitScoreList):
        if((i+1)%2 == 0):
            evenPairs.append(value)
        else:
            oddPairs.append(value)
    
    oddPairsDict = {}
    evenPairsDict = {}
    # for odd in oddPairs:
    #     if(odd[0:1] in oddPairsDict):
    #         if(type(oddPairsDict[odd[0:1]]) == type(list())):
    #             oddPairsDict[odd[0:1]].append(odd)
    #         else:
    #             oddPairsDict[odd[0:1]] = []
    #             oddPairsDict[odd[0:1]].append(odd)
    #     else:
    #         oddPairsDict[odd[0:1]] = []

    print(oddPairs)
    print(evenPairs)
    for odd in oddPairs:
        if(odd[0:1] in oddPairsDict):
            if(type(oddPairsDict[odd[0:1]]) == type(list())):
                oddPairsDict[odd[0:1]].append(odd)
            else:
                oddPairsDict[odd[0:1]] = []
                oddPairsDict[odd[0:1]].append(odd)
        else:
            oddPairsDict[odd[0:1]] = []
            oddPairsDict[odd[0:1]].append(odd)

    for even in evenPairs:
        if(even[0:1] in evenPairsDict):
            if(type(evenPairsDict[even[0:1]]) == type(list())):
                evenPairsDict[even[0:1]].append(even)
            else:
                evenPairsDict[even[0:1]] = []
                evenPairsDict[even[0:1]].append(even)
        else:
            evenPairsDict[even[0:1]] = []
            evenPairsDict[even[0:1]].append(even)
    
    print(oddPairsDict)
    print(evenPairsDict)

    possiblePairs = 0
    for o in oddPairsDict:
        if(len(oddPairsDict[o]) == 2):
            possiblePairs += 1
        elif(len(oddPairsDict[o]) > 2):
            possiblePairs += len(list(combinations(oddPairsDict[o], 2)))
    for e in evenPairsDict:
        if(len(evenPairsDict[e]) == 2):
            possiblePairs += 1
        elif(len(evenPairsDict[e]) > 2):
            possiblePairs += len(list(combinations(evenPairsDict[e], 2)))
            possiblePairs -= 1
    
    print(possiblePairs)

bitScoreList = []

for rawNumber in rawNumbersList:
    bitScoreList.append(calculateBitScore(rawNumber))

print(bitScoreList)
calculateDigitPairs(bitScoreList)