def solution(my_string, queries):
    answer = list(my_string)
    for i in queries:
        for j in range(i[0],(i[1]-i[0])//2+i[0]+1):
            answer[j], answer[i[0]+i[1]-j] = answer[i[0]+i[1]-j], answer[j]
    answer= ''.join(answer)
    return answer