def com(a,b):
    all=(a+b)
    all.sort()
    print(all)
    c=[]
    d=[]
    c.append(all.pop())
    d.append(all.pop())
    while len(all)>0:    
        if sum(d)>sum(c):
            d.append(all.pop(0))
            c.append(all.pop())
        else:
            d.append(all.pop())
            c.append(all.pop(0))
    return c,d
