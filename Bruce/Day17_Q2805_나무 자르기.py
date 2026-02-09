import sys

def equation(x,b):
    if x>b:
        return 0
    return b-x

def solve():
    input = sys.stdin.readline
    N,M = map(int,input().split())   
    a = list(map(int,input().split()))
    g = lambda x: sum(equation(x, i) for i in a)

    left = 0
    right = max(a)
    mids = []
    # 0보다 크면 오른쪽으로 작으면 왼쪽으로 이동하면서 최적값 수정
    while left <=right:
        mid = (left + right) // 2
        mids.append(mid)
        over = g(mid) -M
        if over ==0:
            break
        elif over >0:
            left = mid+1
            
        elif over < 0:
            right = mid-1

    # 최적값, 좌, 우 중 하나가 답이겠지
    x = mids[-1]
    xs = [x-1, x, x+1]
    result = []
    for i in range(3):
        result.append(g(xs[i])-M)

    resultt = [x for x in result if x >= 0]
    print(xs[result.index(min(resultt))])


if __name__ == "__main__":                              
    solve()