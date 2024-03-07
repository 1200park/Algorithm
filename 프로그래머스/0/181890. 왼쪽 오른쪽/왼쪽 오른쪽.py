def solution(str_list):
    answer = []
    
    for x, y in enumerate(str_list):
        if y == "l":
            return str_list[:x]
        
        if y == "r":
            return str_list[x+1:]
    
    return []