tot = 0.00
wk = 4
for i in range(5):
    if wk == 0:
        break
    l = input().split()
    for ii in l:
        if ii=="w":
            wk -= 1
        elif ii.isnumeric():
            tot += int(ii)
        elif ii.isalnum():
            try:
                tot += int(ii[0])
            except:
                tot += 1
if tot / 5 >= 10.00:
    print("Win")
else:
    print("Lose")
