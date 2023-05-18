def findJudge():
    # n=2
    # trust=[[1,3],[2,3],[3,1]]
    # if n == 1:
    #     return 1
    # result = [0] * (n + 1)
    # x = 0
    # y = 0
    # for i in range(len(trust)):
    #     for j in range(len(trust[i]) - 1):
    #         x = trust[i][j]
    #         y = trust[i][j + 1]
    #         result[x] = -1
    #         result[y] += 1
    # maximum = max(result)
    # k = 0
    # for i in range(len(result)):
    #     if result[i] == maximum and k == 0 and maximum != 0:
    #         return i
    # return -1

    n=2
    trust=[[1,2],[2,3]]
    # if n==2 or n==1:
    #     print(n)
    result = [0]*(n+2)
    print(result)
    x = 0
    y = 0
    for i in range(len(trust)):
        for j in range(len(trust[i])-1):
            x = trust[i][j]
            y = trust[i][j + 1] 
            result[x] = -1
            result[y] += 1
    maximum=max(result)
    k=0
    for i in range(len(result)):
        if result[i]==maximum and k==0 and maximum>1:
            print(i)
            k+=1
        if maximum==0:
            print(-1)
            break
    return 0


findJudge()