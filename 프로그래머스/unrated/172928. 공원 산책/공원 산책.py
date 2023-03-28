def solution(park, routes):
    i = 0 
    
    # 시작 지점 찾기 
    for findS in park:
        if "S" in findS:
            start = findS.index("S")
            start = [i,start]
            print("start",start)
            break
        i += 1 
    
    width = int(len(park[0]))
    height =int(len(park))
    print("width",width,"height",height)
    # 길찾기 
    isSuccess = True 
    for route in routes:
        repeat = int(route[2])
        befstart = start.copy()
        for i in range(repeat):
            if route[0] == "N":
                start[0] -= 1 
            if route[0] == "S":
                start[0] += 1 
            if route[0] == "W":
                start[1] -= 1 
            if route[0] == "E":
                start[1] += 1 
            if isValidPoint(park,start,width,height) == False: 
                print("befstart",befstart)
                start = befstart
                break 
        print(start)
    return start 


def isValidPoint(park, start, width, height): 
    if start[0] < 0 or start[1] < 0:
        return False
    if start[0] >= height or start[1] >= width:
        return False
    x = start[0] 
    y = start[1] 
    print(x,y)
    if park[x][y] == "X":
        return False
    
    return True