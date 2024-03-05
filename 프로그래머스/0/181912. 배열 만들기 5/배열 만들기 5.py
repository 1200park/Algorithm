def solution(intStrs, k, s, l):
    answer = []
    
    for i in intStrs:
        arg=''
        for j in range(s,s+l):
            arg += i[j]
        if k < int(arg):
            answer.append(int(arg))
    return answer