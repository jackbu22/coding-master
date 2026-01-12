import sys

def solve():
    Numbers = list(map(int, input().split()))
    a = []
    b = []
    T = []
    for i in range(1,Numbers[0]//2+2):
        if Numbers[0]%i ==0:
            a.append(i)
            a.append(Numbers[0]//i)

    for j in range(1,Numbers[1]//2+2):
        if Numbers[1]%j ==0:
            b.append(j)
            b.append(Numbers[1]//j)
    
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]==b[j]:
                T.append(a[i])

    max_V = max(T)
    min_V = Numbers[0]*Numbers[1]//max_V

    print(max_V, min_V)



if __name__ == "__main__":                              
    solve()