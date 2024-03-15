def solution(order):
    answer = 0
    for idx in order:
        if 'cafelatte' in idx:
            answer += 5000
        else:
            answer += 4500
    return answer