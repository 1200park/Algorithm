def solution(my_string):
    answer = [0]*52
    str = list(my_string)
    for i in str:
        if i.isupper():
            a = ord(i) - 65
        else:
            a = ord(i) - 97 + 26
        answer[a] += 1
    return answer