inputs = []

while True:
    i = input()
    if i == "q":
        break
    newlist = list(map(int, i.split()))
    inputs.append(newlist)
    
    
def isSafe(reactor: list[int]) -> bool:
    threshold = reactor[0] - reactor[1]
    doublecheck1 = reactor[1] - reactor[2]
    doublecheck2 = reactor[2] - reactor[3]
    saftey = True
    if threshold > 0 and doublecheck1 > 0:
        threshold = 1
        maxThresh = 3
        d = False
    elif threshold < 0 and doublecheck2 < 0:
        threshold = -1
        maxThresh = -3
        d = True
    else:
        threshold = 1
        maxThresh = 3
        d = False
    # d is True for increasing, False for decreasing
    #print(maxThresh)
    #print(threshold)
    i = 1
    while i < len(reactor):
        dif = reactor[i - 1] - reactor[i]
        #print(reactor[i-1],reactor[i])
        if d:
            if (maxThresh <= dif and threshold >= dif):
                i += 1
                continue
            else:
                #(dif, i)
                if saftey:
                    #print(reactor)
                    #print("TRIGGER UP")
                    saftey = False
                    reactor.remove(reactor[i])
                    continue
                #print("REJECTED")
                return False
        else:
            if (maxThresh >= dif and threshold <= dif):
                i += 1
                continue
            else:
                if saftey:
                    # print(reactor)
                    # print("TRIGGER DOWN")
                    saftey = False
                    reactor.remove(reactor[i])
                    continue
                #print("REJECTED")
                return False
        
    return True
    
safeNum = 0
for i in inputs:
    if isSafe(i):
        safeNum += 1

print(safeNum)


    
