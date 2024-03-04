def solution(n):
    answer = []
    
    while n>=1:
        answer.append(n)
        if n%2 ==0:
            n /= 2
        elif n%2 == 1 and n >1:
            n = 3*n +1
        else:
            break
    return answer