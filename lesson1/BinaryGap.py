def solution(N):
    # write your code in Python 2.7
    bStr = str(bin(N))
    i=2
    distList=[]
    while i<(len(bStr)):
        if bStr[i]=='1':
            distList.append(i)
        i += 1
    maxDist=0
    for i in range(1,len(distList)):
        currentDist = distList[i]-distList[i-1]-1
        if maxDist < currentDist:
            maxDist = currentDist
    return maxDist

if __name__ == '__main__':
    # solution(9)
    print(solution(529))