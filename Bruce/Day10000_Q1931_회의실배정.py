import sys

def solve():
    input = sys.stdin.readline

    N = int(input())
    starts = []
    ends =[]
    for _ in range(N):
        a,b = map(int, input().split())
        if a in starts:
            index = starts.index(a)
            if ends[index] > b:
                ends[index] = b
        else:
            starts.append(a)
            ends.append(b)
    
    timetable = []
    for i in range(len(starts)):
        sumss = dict()
        sumss["x"] = starts[i]
        sumss["y"] = ends[i]
        timetable.append(sumss)
    sorted_timetable = sorted(timetable, key=lambda s: s["x"])

    print(sorted_timetable)
    onoff = []
    for i in range(len(sorted_timetable)-1):
        if sorted_timetable[i]['x'] < sorted_timetable[i+1]['x'] and sorted_timetable[i]['y'] > sorted_timetable[i+1]['y']:
            onoff.append(0)
        else:
            onoff.append(1)
        
        



if __name__ == "__main__":
    solve()