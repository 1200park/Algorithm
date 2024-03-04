def solution(l, r):
    answer = []
    
    for i in range(l,r+1):
        arg=list(str(i))
        k=0
        for j in arg:
            if j =="5" or j=="0":
                k +=1
        if k == len(arg):
            answer.append(i)
    if len(answer) == 0: answer.append(-1)
    return answer