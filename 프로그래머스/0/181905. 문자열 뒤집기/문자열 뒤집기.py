def solution(my_string, s, e):
    
    answer = my_string[:s] + my_string[e:s:-1] + my_string[s] + my_string[e+1:]
    
    return answer