def insertel(x):
    x.insert(0,'red')
    x.insert(2,'green')
    x.insert(4,'black')
    print(x)
insertel([1,2,3])

def sort(x):
    y = []
    for i in range(len(x)):
        y.append(min(x))
        x.remove(min(x))
    print(y)
sort([1,4,6,2,46])
