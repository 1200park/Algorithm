def solution(data, ext, val_ext, sort_by):
    answer = []
    
    if ext=='code':
        for i in data:
            if i[0]<val_ext:
                answer.append(i)
    elif ext=='date':
        for i in data:
            if i[1]<val_ext:
                answer.append(i)
    elif ext=='maximum':
        for i in data:
            if i[2]<val_ext:
                answer.append(i)
                
    else:
        for i in data:
            if i[3]<val_ext:
                answer.append(i)
                
    if sort_by=='code':
        answer=sorted(answer, key=lambda x: x[0])
    elif sort_by=='date':
        answer=sorted(answer, key=lambda x: x[1])
    elif sort_by=='maximum':
        answer=sorted(answer, key=lambda x: x[2])
    else:
        answer=sorted(answer, key=lambda x: x[3])
    
    return answer