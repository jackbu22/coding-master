import sys
import math

# 1차원 리스트를 nxn array로 변경
def array(a):
    x = int(math.sqrt(len(a)))
    arr = []
    for _ in range(x):
        arr.append([])
    for i in range(len(a)):
        length = i//x
        arr[length].append(a[i])

    return arr

# nxn array를 4개의 array로 바꿈
def divide(list):
    step = []
    for i in range(4):
        step.append([])
    K = len(list[0])
    for i in range(K):
        for j in range(K):
            if i < K//2 and  j < K//2:
                step[0].append(list[i][j])
            elif i < K//2 and j >= K//2:
                step[1].append(list[i][j])
            elif i >= K//2 and j < K//2:
                step[2].append(list[i][j])
            else:
                step[3].append(list[i][j])

    return step

# 4개의 array에 대해 black, white를 판단
def decide(step):
    black = 0
    white = 0
    erase = []
    for i in range(4):
        x = step[i][0]
        if len(set(step[i])) == 1:
            if x==1:
                black +=1
            else:
                white +=1
            erase.append(i)
    erase.sort(reverse = True)
    for i in erase:
        del step[i]
    return step, black, white

def solve():
    black = 0
    white = 0

    input = sys.stdin.readline
    whole = [] 
    N = int(input())    
    count = int(math.log(N,2))

    # 여러개의 숫자를 받아서 1차원 리스트로 만듬
    for i in range(N):
        a = list(map(int,input().split()))
        whole.append(a)
    whole = sum(whole,[])
    x = []
    x.append(whole)
    whole = x
    
    whole_if = set(whole[0])
    
    if len(whole_if)==1:
        whole_if = list(whole_if)
        if whole_if[0]==1:
            print(0)
            print(1)
        else:
            print(1)
            print(0)
    else:
        while count !=0:
            news = []
            for i in range(len(whole)):
                whole_1 = array(whole[i])
                whole_2 = divide(whole_1)
                new,b,w = decide(whole_2)
                if len(new)!=0:
                    for i in range(len(new)):
                        news.append(new[i])
                black += b
                white += w
            whole = news
            count-=1
        
        print(white)
        print(black)

if __name__ == "__main__":                              
    solve()