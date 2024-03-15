def solution(myString):
    answer = ''
    for idx in myString:
        if ord(idx) <= ord('l'):
            answer += "l"
        else:
            answer += idx
    return answer