x=[1,2,3]
y=[2,3,4]
for i in y:
    for j in x:
        if i==j:
            x.remove(j)
print(x)
