# 시작전 알고리즘 구상
#   결과를 저장할 리스트1 
#   반복문1을 통해 3개의 숫자 입력 -> 0 0 0이 나올 때 까지
#   반복문1에서 a^2+b^2=c^2임을 확인 후 맞으면 right, 틀리면 wrong을 리스트1에 저장
#   리스트1을 출력형식을 변경하여 출력

import sys

def solve():
    result = []
    n = 0
    while True:
        input = sys.stdin.readline
        Z = list(map(int, input().split()))
        if Z[0] ==0 and Z[1] ==0 and Z[2] ==0:
            break
        else:
            Z.sort()
            if Z[0]**2+Z[1]**2 == Z[2]**2:
                print("Right")
            else:
                print("Wrong")
            

if __name__ == "__main__":                              
    solve()