def removedup(x):
    y = []
    for i in x:
        if i not in y:
            y.append(i)
    print (y)
removedup([1,2,3,4,4,1,5]
