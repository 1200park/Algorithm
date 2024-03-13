def solution(arr, flag):
    answer = []
    for i, boo in enumerate(flag):
        if boo:
            for _ in range(arr[i]*2):
                answer.append(arr[i])
                
        else:
            for _ in range(arr[i]):
                answer.pop()
    return answer