x=input()
if(x.isnumeric()): 
    n=int(x)

    if(1<=n and n<=1000):
        for i in range(1,13):
            print(n,end="")
            print(" x ",end="")
            if(i<=9):
                print("0",end="")
                print(i,end="")
                print(" = ",end="")
                print(i*n)
            else:
                print(i,end="")
                print(" = ",end="")
                print(i*n)
