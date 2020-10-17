import re

n=int(input())
if(0<=n and n<=100000):
    for i in range(n):
        x=input()
        p=r'^[a-zA-z0-9]{4,10}@nanolabs[\.]\b(com|dev|crew)\b[\.]\b(au|de|fr|hk|id|in|jp|lk|mm|nz|ru|uk|us|vn)\b$'
        if bool(re.match(p,x))==True:
            print("ALLOWED")
        else:
            print("BLOCKED")
