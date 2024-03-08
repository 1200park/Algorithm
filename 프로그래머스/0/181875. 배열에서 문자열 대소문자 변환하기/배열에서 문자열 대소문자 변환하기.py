def solution(strArr):
    answer = []
    for i in strArr:
        if strArr.index(i)%2 == 1:
            answer.append(i.upper())
        else:
            answer.append(i.lower())
    return answer