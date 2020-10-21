try:
    n = int(input())
    if n>=1 and n<=10**3:
        for i in range(1,13):
            if i < 10:
                print(str(n) + " " + "x" + " " + "0" + str(i) + " " + "=" + " " + str(n * i))
            else:
                print(str(n) + " " + "x" + " " + str(i) + " " + "=" + " " + str(n * i))
except:pass
