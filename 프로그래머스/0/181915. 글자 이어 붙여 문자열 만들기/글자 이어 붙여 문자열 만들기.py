def solution(my_string, index_list):
    answer = ''
    
    for i in index_list:
        answer=''.join([answer,my_string[i]])
    return answer