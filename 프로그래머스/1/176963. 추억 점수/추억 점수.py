def solution(name, yearning, photo):
    answer = []
    for i in photo:
        sum=0
        for j in range(len(name)):
            if name[j] in i:
                sum+=yearning[j]
        answer.append(sum)
    return answer