aa = int(input())
a = list(map(int,input().split()))

a.sort()
if len(a) > 1 and len(a) < 1000:
    l = []
    for i in range(1,6):
        l.append(str(a.count(i)))

    print(" ".join(l))
else:
    l = ['0','0','0','0','0']
    print(" ".join(l))
