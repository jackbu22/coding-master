import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    Scores = list(map(int, input().split()))
    M = max(Scores)

    for i in range(len(Scores)):
        Scores[i] = Scores[i]/M*100
    
    print(sum(Scores)/N)




if __name__ == "__main__":                              
    solve()