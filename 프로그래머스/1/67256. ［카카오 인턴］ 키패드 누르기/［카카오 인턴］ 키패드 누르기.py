def solution(numbers, hand):
    answer = ''
    
    numbers = [11 if x == 0 else x for x in numbers]
    left = [1,4,7]
    right = [3,6,9]
    middle = [2,5,8,0]
    left_hand = [0,3]
    right_hand = [2,3]
    
    lab = [[] for i in range(12)]
    lab[2] = [1,0]
    lab[5] = [1,1]
    lab[8] = [1,2]
    lab[11] = [1,3]
    
    for num in numbers:
        if num in left:
            answer += 'L'
            left_hand = [0,(num-1)/3]
        elif num in right:
            answer += 'R'
            right_hand = [2,(num-3)/3]
        else:
            if abs(left_hand[0]-lab[num][0]) + abs(left_hand[1]-lab[num][1]) < abs(right_hand[0]-lab[num][0]) + abs(right_hand[1]-lab[num][1]):
                left_hand = [1, (num-2)/3]
                answer += 'L'
            elif abs(left_hand[0]-lab[num][0]) + abs(left_hand[1]-lab[num][1]) > abs(right_hand[0]-lab[num][0]) + abs(right_hand[1]-lab[num][1]):
                right_hand = [1, (num-2)/3]
                answer += 'R'
            else:
                if hand == 'left':
                    left_hand = [1, (num-2)/3]
                    answer += 'L'
                else:
                    right_hand = [1, (num-2)/3]
                    answer += 'R'
            
    return answer