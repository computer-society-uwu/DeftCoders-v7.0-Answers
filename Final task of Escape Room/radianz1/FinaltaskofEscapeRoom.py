NO_OF_CHARS = 10000

def canFormPalindrome(string): 
      
    count = [0 for i in range(NO_OF_CHARS)] 
    for i in string: 
        count[ord(i)] += 1 
    odd = 0
    for i in range(NO_OF_CHARS): 
        if (count[i] & 1): 
            odd += 1
   
        if (odd > 1): 
            return False
    return True
s = input()
if(s.islower()):
    if(canFormPalindrome(s)): 
        print("YES") 
    else: 
        print("NO")
else:
    print("NO")
