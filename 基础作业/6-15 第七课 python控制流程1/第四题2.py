x=[1,2,3,4,5]
y=[1,2,3]
for i in y:
    for j in x:
        if i==j:
            x.remove(j)
print(x)
