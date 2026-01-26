import sys

def solve():
    input = sys.stdin.readline

    N = int(input())
    sets = set()

    for i in range(N):
        func = input().split()
        if func[0] == "add":
            sets.add(int(func[1]))

        elif func[0] == "remove":
            sets.discard(int(func[1]))

        elif func[0] == "check":
            if int(func[1]) in sets:
                print(1)
            else:
                print(0)

        elif func[0] == "toggle":
            if int(func[1]) in sets:
                sets.discard(int(func[1]))
            else:
                sets.add(int(func[1]))

        elif func[0] == "all" :
            sets = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
        elif func[0] == "empty" :
            sets.clear()



    


if __name__ == "__main__":
    solve()