def solution(arr, queries):
    answer = arr
    for j in queries:
        for i in range(j[0],j[1]+1):
            if i%j[2]==0:
                answer[i] += 1
    return answer