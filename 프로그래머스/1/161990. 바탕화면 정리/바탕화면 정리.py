def solution(wallpaper):
    answer = []
    
    lux = 0
    for i in wallpaper:
        if "#" in i:
            break
        lux += 1
    answer.append(lux)
    
    luy = 50 
    for i in wallpaper:
        if '#' in i and i.index("#") < luy:
            luy = i.index("#")
    answer.append(luy)
    
    rdx = len(wallpaper)
    for i in wallpaper[::-1]:
        if "#" in i:
            break
        rdx -= 1
    answer.append(rdx)
        
    rdy = 0
    for i in wallpaper:
        if '#' in i and rdy < i.rfind("#")+1:
            rdy = i.rfind("#")+1
    answer.append(rdy)
    
    return answer