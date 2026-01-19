import sys

def solve():

    input = sys.stdin.readline
    N = int(input())            # 괄호의 수

    for i in range(N):
        each = [] 
        NM = input().strip()
        for i in range(len(NM)):
            if NM[i] == '(':
                each.append(1)
            elif NM[i] == ')':
                each.append(-1)
        if sum(each) != 0:
            print("NO")
            continue
        
        sumss = []
        for i in range(len(each)):
            sumss.append(sum(each[0:i+1]))
        
        if any(x < 0 for x in sumss):
            print("NO")
        else:
            print("YES")

if __name__ == "__main__":                              
    solve()