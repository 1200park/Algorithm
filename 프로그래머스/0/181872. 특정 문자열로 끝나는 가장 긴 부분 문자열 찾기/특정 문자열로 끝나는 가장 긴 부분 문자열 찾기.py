def solution(myString, pat):
    answer = ''
    
    myString1 = myString[::-1]
    pat1 = pat[::-1]
    
    idx = len(myString1) - myString1.index(pat1)
    
    answer = myString[:idx]
    
    return answer