'''자연수 
\(N\)과 정수 
\(K\)가 주어졌을 때 이항 계수 
\(\binom{N}{K}\)를 구하는 프로그램을 작성하시오.'''

# import math

n, k = map(int, input().split())

# fac = math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

result_n = 1
result_k = 1
re_nk= 1


for i in range (1, n + 1):
    result_n *= i
    print(result_n)
    
for i in range(1, k + 1):
    result_k *= i
    print(result_k)
    
for i in range (1, n - k + 1):   
    re_nk *= i
    print(re_nk)

print(result_n // (result_k * re_nk))

