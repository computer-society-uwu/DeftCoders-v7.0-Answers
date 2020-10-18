x=input()

NO = 256

def canFormPalindrome(st) : 

    count = [0] * (NO) 

    for i in range( 0, len(st)) : 
        count[ord(st[i])] = count[ord(st[i])] + 1

    odd = 0
    
    for i in range(0, NO) : 
        if (count[i] & 1) : 
            odd = odd + 1

        if (odd > 1) : 
            return False

    return True

if(canFormPalindrome(x)) : 
    print("YES") 
else : 
    print("NO") 
    
 
