s = input()
tot = 0
vowels = ["a","e","i","o","u"]
for i in vowels:
    tot = tot + s.lower().count(i)
    
print(tot)
