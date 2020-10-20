n = int(input())
if n >= 0 and n <= 10**5:
    l = ['au','de','fr','hk','id','in','jp','lk','mm','nz','ru','uk','us','vn']
    ll = ['com','dev','crew']
    for i in range(n):
        email = input().split(".")
        if len(email) == 3:
            if email[1] in ll:
                if email[2] in l:
                    t = email[0].split('@')
                    if t[1] == "nanolabs":
                        if t[0].isalnum() and (len(t[0]) >= 4 and len(t[0]) <=10):
                            print("ALLOWED")
                        else:
                            print("BLOCKED")
                    else:
                        print("BLOCKED")
                else:
                    print("BLOCKED")
            else:
                print("BLOCKED")
        elif len(email) == 2:
            if email[1] == "com":
                t = email[0].split('@')
                if t[0].isalnum() and (len(t[0]) >= 4 and len(t[0]) <=10):
                            print("ALLOWED")
                else:
                    print("BLOCKED")
            else:print("BLOCKED")
        else:print("BLOCKED")
