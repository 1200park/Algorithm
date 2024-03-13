def solution(arr):
    answer = []
    for i, num in enumerate(arr):
        if len(answer) == 0:
            answer.append(num)
        else:
            if answer[-1] == num:
                answer.pop()
            else:
                answer.append(num)
    return answer if answer else [-1]