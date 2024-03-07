def solution(todo_list, finished):
    answer = []
    
    for idx, ans in enumerate(finished):
        if ans == False:
            answer.append(todo_list[idx])
    return answer