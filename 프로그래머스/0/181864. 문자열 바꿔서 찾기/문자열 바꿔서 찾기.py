def solution(myString, pat):
    answer = 0
    new = ""
    for i in myString:
        if i == "A":
            new = ''.join([new,"B"])
        else:
            new = ''.join([new,"A"])
    if pat in new:
        answer = 1
    return answer