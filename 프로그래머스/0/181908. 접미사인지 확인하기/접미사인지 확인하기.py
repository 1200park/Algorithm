def solution(my_string, is_suffix):
    answer = 0
    arg=[]
    
    for i in range(len(my_string)):
        arg.append(my_string[i:])
        
    if is_suffix in arg:
        answer = 1
    else: answer = 0
    
    return answer