import sys

def solve():

    input = sys.stdin.readline
    N = int(input())           

    Coordinate =[]
    xs = []
    for i in range(N):
        x , y = input().split()
        dict = {}
        dict["x"] = int(x)
        dict["y"] = int(y)
        Coordinate.append(dict)
        xs.append(int(x))
    xs = list(set(xs))  
    xs.sort()
    Max_x = max(xs)
    Min_x = min(xs)


    xss = []
    for i in range(Min_x , Max_x+1):
        xss.append([])
    
    for i in range(len(xss)): 
        for j in range(len(Coordinate)):
            if Coordinate[j]["x"]-Min_x == i :
                xss[i].append(Coordinate[j]["y"])

    for i in range(len(xss)):
        xss[i].sort()
    
    for i in range(len(xss)):
        for j in range(len(xss[i])):
            if len(xss[i])!=0:
                print(i+Min_x, xss[i][j])

if __name__ == "__main__":                              
    solve()