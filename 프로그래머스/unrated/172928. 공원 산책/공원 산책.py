def solution(park, routes):
    i = 0 
    for findS in park:
        if "S" in findS:
            start = findS.index("S")
            start = [i,start]
            break
        i += 1 
    
    width = len(routes[0])
    height = len(routes)
    
    for route in routes:
        befstart = start.copy()
        print(start)
        
        if route[0] == "E":
            start[1] += int(route[2])
        elif route[0] == "S":
            start[0] += int(route[2])
        elif route[0] == "W":
            start[1] -= int(route[2])
        elif route[0] == "N":
            start[0] -= int(route[2])
        first = start[0]
        second = start[1]
        if park[first][second] == "X":
            start = befstart
        
        
        
        if start[0] < 0 or start[1] < 0 or start[0] >= width or start[1] >= height : 
            print("befstart",befstart)
            start = befstart 
        
        
    return start 