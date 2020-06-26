def squareddict(n):
    dict = {}
    for i in range(1,n+1):
        dict[i]= i**2
    print(dict)
squareddict(5)
    
def sortval(n):
    print(sorted(n.items(),key=lambda x:x[1], reverse = True))
sortval({'Math':81, 'Physics':83, 'Chemistry':87})
