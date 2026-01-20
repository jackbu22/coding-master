import sys

def solve():

    input = sys.stdin.readline
    N, M = map(int, input().split())

    WBs =[]
    for i in range(N):
        WB = list(input().strip())
        WBs.append(WB)

    answer = 100
    for i in range(N-7):
        for j in range(M-7):
            candidate = 0
            for k in range(i,i+8):
                for z in range(j,j+8):
                    if (k+z)%2 ==0:
                        if WBs[k][z] == 'B':
                            candidate+=1
                    elif (k+z)%2 ==1:
                        if WBs[k][z] == 'W':
                            candidate+=1
            if min(candidate,64-candidate) < answer:
                answer = min(candidate,64-candidate)

    print(answer)
   


if __name__ == "__main__":
    solve()

