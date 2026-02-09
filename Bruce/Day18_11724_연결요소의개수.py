import sys

def solve():
    input = sys.stdin.readline
    N,M = map(int, input().split())          
    
    # 간선을 오름차순으로 정렬
    connects = []
    for i in range(M):
        connect = []
        a,b = map(int, input().split())
        connect.append(min(a,b))
        connect.append(max(a,b))
        connects.append(connect)
    sorted_connects = sorted(connects, key=lambda x: x[0])

    # {1:1, 2:2, 3:3, 4:4 ...} 생성
    result = {}
    for i in range(1,N+1):
        result[i] = [i]

    for i in range(M):
        a = sorted_connects[i][0]
        b = sorted_connects[i][1]
        from_index = 0
        to_index = 0
        for k, v in result.items():
            if a in v:
                from_index = k
            if b in v:
                to_index = k

        if from_index==to_index:
            continue
        result[from_index].extend(result[to_index])

        del result[to_index]

    print(len(result))

if __name__ == "__main__":                              
    solve()