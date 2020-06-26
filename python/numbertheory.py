def  sumdivisors(d):
    x = 0
    for i in range(1,d):
        if d%i == 0:
            x += i
    return x
print(sumdivisors(284))
def amicablenums(a,b):
    if sumdivisors(a) == b  and sumdivisors(b) == a:
        print(a, 'and', b, 'are amicable numbers')
    else:
        print('Not amicable numbers')
amicablenums(220,284)
