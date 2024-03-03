def solution(cards1, cards2, goal):
    answer = ''
    x = 0
    y = 0
    result = []  # 변수명 수정
    
    for i in range(len(goal)):
        if x < len(cards1) and goal[i] == cards1[x]:  # x가 cards1의 길이보다 작을 때만 cards1 접근
            result.append(cards1[x])
            x += 1
                
        elif y < len(cards2) and goal[i] == cards2[y]:  # y가 cards2의 길이보다 작을 때만 cards2 접근
            result.append(cards2[y])
            y += 1
                
        else:
            break
            
    if result == goal:  # 모든 요소가 일치하는지 확인
        answer = "Yes"
    else:
        answer = "No"
        
    return answer
