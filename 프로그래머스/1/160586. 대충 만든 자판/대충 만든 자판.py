def solution(keymap, targets):
    answer = []
    
    for i in targets:
        total_index_sum = 0
        
        for j in i:
            idx = 100
            for k in keymap:
                if j in k and k.index(j)+1 < idx:
                    idx = k.index(j)+1
            
            if idx == 100:
                total_index_sum = -1
                break
            
            total_index_sum += idx
        
        
        answer.append(total_index_sum)
        
    return answer
