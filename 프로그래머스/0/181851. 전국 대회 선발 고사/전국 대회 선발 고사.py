def solution(rank, attendance):
    answer = 0
    arr = []
    arg = []
    for i in range(len(rank)):
        arr.append((rank[i],attendance[i],i))
    arr.sort()  
    for a, b, c in arr:
        if b:
            arg.append(c)
        if len(arg) == 3:
            break
            
    answer = 10000*arg[0] + 100*arg[1] + arg[2]
            
    return answer