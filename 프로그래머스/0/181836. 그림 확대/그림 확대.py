def solution(picture, k):
    answer = []
    for idx in picture:
        str = ''
        for i in idx:
            for _ in range(k):
                str += i
        for _ in range(k):
            answer.append(str)
    return answer