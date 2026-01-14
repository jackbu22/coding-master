'''
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
'''

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    result = 0

    for num in nums:
        cnt = 0
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    cnt += 1
            
            if cnt == 0:
                result += 1
        
    print(result)

if __name__ == "__main__":
    main()