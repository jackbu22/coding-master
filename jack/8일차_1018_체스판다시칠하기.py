# 문제
# 지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다. 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.

# 체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

# 보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.

# 출력
# 첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.

# 예제 입력 1 
# 8 8
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBBBWBW
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBWBWBW
# 예제 출력 1 
# 1
# 예제 입력 2 
# 10 13
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# WWWWWWWWWWBWB
# WWWWWWWWWWBWB
# 예제 출력 2 
# 12
# 예제 입력 3 
# 8 8
# BWBWBWBW
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# 예제 출력 3 
# 0
# 예제 입력 4 
# 9 23
# BBBBBBBBBBBBBBBBBBBBBBB
# BBBBBBBBBBBBBBBBBBBBBBB
# BBBBBBBBBBBBBBBBBBBBBBB
# BBBBBBBBBBBBBBBBBBBBBBB
# BBBBBBBBBBBBBBBBBBBBBBB
# BBBBBBBBBBBBBBBBBBBBBBB
# BBBBBBBBBBBBBBBBBBBBBBB
# BBBBBBBBBBBBBBBBBBBBBBB
# BBBBBBBBBBBBBBBBBBBBBBW
# 예제 출력 4 
# 31
# 예제 입력 5 
# 10 10
# BBBBBBBBBB
# BBWBWBWBWB
# BWBWBWBWBB
# BBWBWBWBWB
# BWBWBWBWBB
# BBWBWBWBWB
# BWBWBWBWBB
# BBWBWBWBWB
# BWBWBWBWBB
# BBBBBBBBBB
# 예제 출력 5 
# 0
# 예제 입력 6 
# 8 8
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBBBWBW
# WBWBWBWB
# BWBWBWBW
# WBWBWWWB
# BWBWBWBW
# 예제 출력 6 
# 2
# 예제 입력 7 
# 11 12
# BWWBWWBWWBWW
# BWWBWBBWWBWW
# WBWWBWBBWWBW
# BWWBWBBWWBWW
# WBWWBWBBWWBW
# BWWBWBBWWBWW
# WBWWBWBBWWBW
# BWWBWBWWWBWW
# WBWWBWBBWWBW
# BWWBWBBWWBWW
# WBWWBWBBWWBW
# 예제 출력 7 
# 15

import sys

input=sys.stdin.readline

a,b= map(int,input().split())
c=[]
me_w = "WBWBWBWB"#,'bwbwbwbw','wbwbwbwb','bwbwbwbw','wbwbwbwb','bwbwbwbw','wbwbwbwb','bwbwbwbw']
me_b = "BWBWBWBW"#,'wbwbwbwb','bwbwbwbw','wbwbwbwb','bwbwbwbw','wbwbwbwb','bwbwbwbw','wbwbwbwb']


# print(a,b)


for i in range(a):
    d=input()
    c.append(d[:-1])
# print(c)
answer_w=[]
answer_b=[]
for i in range(a-8+1):# 시작 어디 행을 볼껀지 
    d=c[i:i+8] 
    for j in range(b-8+1):#행에서 어디 열을 처음으로 볼껀지
        for k in range(8):#행별로 어디서 시작할지
            e=d[k][j:j+8]
            for p in range(2):
                if p==0:    
                    if k%2==0:
                        answer_w.append(sum(1 for a, b in zip(e, me_w) if a != b))
                    elif k%2!=0:
                        
                        answer_w.append(sum(1 for a, b in zip(e, me_b) if a != b))
                if p ==1:
                    if k%2==0:
                        answer_b.append(sum(1 for a, b in zip(e, me_b) if a != b))
                    elif k%2!=0:
                        answer_b.append(sum(1 for a, b in zip(e, me_w) if a != b))

# print(answer_b,answer_w)

real_answer=[]
for i in range(len(answer_b)//8):
    x=answer_b[i*8:(i+1)*8]
    a=0
    b=0
    for j in x:
        a+=int(j)
    real_answer.append(a)
    y=answer_w[i*8:(i+1)*8]
    for k in y:
        b+=int(k)
    real_answer.append(b)
real_answer.sort()
print(real_answer[0])

        