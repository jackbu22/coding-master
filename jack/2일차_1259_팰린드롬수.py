import sys
input= sys.stdin.readline

while True:
    line = input().strip()
    if line=='0':
        break

    if len(line)%2==0:
        # line='0'+line
        line_trans=''
        line_trans=line_trans.join(reversed(line))
        # print(line_trans)
        if line==line_trans:
            print('yes')
        elif line!=line_trans:
            print('no')
        

    elif len(line)%2!=0:
        line_trans=''
        line_trans=line_trans.join(reversed(line))
        if line==line_trans:
            print('yes')
        elif line!=line_trans:
            print('no')


        


