s = input().lower()
ss = s.split()
ll = []
cp = ["but", "or", "nor","with", "to", "for", "at", "and", "of", "a", "an", "the"]
for i in ss:
    if i not in cp:
        ll.append(i[0].upper() + i[1:])
    else:
        ll.append(i)
    
       
print(" ".join(ll))
