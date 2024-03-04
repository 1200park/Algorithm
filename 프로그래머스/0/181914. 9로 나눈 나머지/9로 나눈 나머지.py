def solution(number):
    answer = 0
    arg = list(number)
    sum=0
    for i in arg:
        sum += int(i)
    answer = sum % 9
    return answer