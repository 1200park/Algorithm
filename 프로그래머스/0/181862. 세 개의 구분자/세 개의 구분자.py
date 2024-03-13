def solution(myStr):
    answer = []
    temp_str = ''
    for i, char in enumerate(myStr):
        if char in ["a", "b", "c"]:
            if temp_str:
                answer.append(temp_str)
                temp_str = ''
                
        elif i < len(myStr) - 1:
            temp_str += char
            
        else:
            temp_str += char
            answer.append(temp_str)
    return answer if answer else ["EMPTY"]

