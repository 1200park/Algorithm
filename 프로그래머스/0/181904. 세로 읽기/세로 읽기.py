def solution(my_string, m, c):
    answer = ''
    arg = []
    
    for i in range(0,len(my_string),m):
        arg.append(my_string[i:i+m])
    
    for j in range(len(arg)):
        answer += arg[j][c-1]
        
    return answer