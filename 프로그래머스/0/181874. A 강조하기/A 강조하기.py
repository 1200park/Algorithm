def solution(myString):
    answer = ''
    for i in myString:
        if i == 'a':
            answer = ''.join([answer,i.upper()])
        elif i.isupper() and i != "A":
            answer = ''.join([answer,i.lower()])
        else:
            answer = ''.join([answer,i])
    return answer