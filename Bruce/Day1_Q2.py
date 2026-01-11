# 참가자의 수 N 입력
# 각 사이즈 별 사람 수 입력 
# 묶음 당 티셔츠 수 T 입력, 묶음 당 자루 수 P입력

import sys
import math

def solve():
    input = sys.stdin.readline
    N = int(input())
    Size = list(map(int, input().split()))
    if sum(Size) != N:
        raise ValueError("인원수가 다릅니다")
    Bundle = list(map(int, input().split()))
    T = 0
    for i in range(len(Size)):
        T += math.ceil(Size[i]/Bundle[0])
    
    print(T)

    a,b = divmod(N,Bundle[1])
    print(a,b)

if __name__ == "__main__":                              
    solve()