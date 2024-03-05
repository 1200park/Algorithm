def solution(my_strings, parts):
    answer = ''
    k=0
    for i in parts:
        for j in range(i[0],i[1]+1):
            answer += my_strings[k][j]
        k += 1
    return answer