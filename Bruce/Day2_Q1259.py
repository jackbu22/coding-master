
import sys

def solve():
    while True:
        input = sys.stdin.readline
        N = int(input())
        if N==0:
            break
        Ns = str(N)
        Nss = []
        RN =0
        for i in range(len(Ns)):
            Nss.append(Ns[i])
        for j in range(len(Nss)):
            RN += int(Nss[j])*10**j
            
        
        if N == RN:
            print('yes')
        else:
            print('no')


if __name__ == "__main__":                              
    solve()
