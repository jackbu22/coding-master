import sys

def solve():

    input = sys.stdin.readline
    N = int(input())            # 사람들의 수

    People =[]
    for i in range(N):
        age , name = input().split()
        dict = {}
        dict["name"] = name
        dict["age"] = int(age)
        People.append(dict)
    
    Max_age = 0
    for i in range(len(People)):
        if Max_age < People[i]["age"]:
            Max_age = People[i]["age"]

    Ages = []
    for i in range(Max_age):
        Ages.append([])
    
    for i in range(len(Ages)): 
        for j in range(len(People)):
            if People[j]["age"]-1 == i :
                Ages[i].append(People[j]["name"])
        
    for i in range(len(Ages)):
        for j in range(len(Ages[i])):
            print(i+1, Ages[i][j])
        
  

if __name__ == "__main__":                              
    solve()