def difference():
    l1 = ['a','b','c','d']
    l2= ['b','d','e','f']
    missing = []
    additional = []
    for i in l1:
        if i not in l2:
            missing.append(i)
    for i in l2:
        if i not in l1:
            additional.append(i)
    print 'Missing values in second list', missing
    print 'Additional values in second list', additional
difference()
