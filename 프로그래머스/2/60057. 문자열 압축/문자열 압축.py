def solution(s):
    if len(s) == 1:
        return 1
    
    answer = len(s)  
    
    for step in range(1, len(s)//2 + 1):  
        compressed = ""  
        prev = s[0:step]  
        count = 1  
        
        for j in range(step, len(s), step):
            current = s[j:j+step]  
            
            if prev == current:  
                count += 1
            else:  
                compressed += str(count) + prev if count >= 2 else prev 
                prev = current  
                count = 1  
                
        compressed += str(count) + prev if count >= 2 else prev  
        
        answer = min(answer, len(compressed))  
        
    return answer
