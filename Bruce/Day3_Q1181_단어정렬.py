import sys

def solve():

    input = sys.stdin.readline
    N = int(input())
    words = []
    count =0
    while count<N:                              #입력
        word = sys.stdin.readline().strip()
        words.append(word)
        count+=1

    words = list(set(words))                    #중복 제거
    N = len(words)

    max_length = 0

    for i in range(len(words)):                         # 가장 긴 단어 출력
        m_length = len(words[i])
        if max_length < m_length:
            max_length = m_length

    divide_lengths = []                                # 길이가 같은 리스트 추가
    for i in range(max_length):
        divide_lengths.append([])
    
    
    for i in range(len(words)):
        divide_lengths[len(words[i])-1].append(words[i])

    sort_words = []
    for i in range(len(divide_lengths)):
        if len(divide_lengths[i])!=0:
            divide_lengths[i].sort()
            sort_words.append(divide_lengths[i])      

    for i in range(len(sort_words)):
        for j in range(len(sort_words[i])):
            print(sort_words[i][j])


if __name__ == "__main__":                              
    solve()