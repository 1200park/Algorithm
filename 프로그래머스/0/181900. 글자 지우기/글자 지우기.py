def solution(my_string, indices):
    answer = list(my_string)
    for i in indices:
        answer[i] = '0'
    k=""    
    for j in answer:
        if j != '0':
            k = ''.join([k,j])
    return k