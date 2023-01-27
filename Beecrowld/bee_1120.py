d = int(input())
n = int(input())


res = str(n).replace(str(d), '')
if(res == ''):
    print(int(0))
else:
    print(int(res))