a = int(input())
c = 0
for i in range(a):
    s = input()
    if 'X' in s:
        print(str(c) + "," + str(s.index('X')))
    c += 1
