
def fruits():
    lst = ['Apple', 'Pear', 'Orange' , 'Peach', 'Cherry', 'Banana' , 'Strawberry']
    a = input('What fruit do you want to add:')
    lst.append(a)
    print(lst)
    b = int(input('What index:'))
    print(lst[b])
    c = input('Add a fruit to the front:')
    lst.insert(0,c)
    print(lst)
    lst.reverse()
    lst.remove(lst[0])
    lst.reverse()
    print(lst)
    d = input('What fruit:')
    print(lst.index(d)+1)
fruits()

def fruitspt2():
    lst = ['Apple', 'Pear', 'Orange' , 'Peach', 'Cherry', 'Banana' , 'Strawberry']
    plst = []
    nopears = []
    for i in lst:
        if i.startswith('P') or i.startswith('p'):
            plst.append(i)
    print(plst)
    for i in range(len(lst)):
        lst.insert(i * 2, "Apple")
    print(lst)
    for i in lst:
        if i == 'Pear':
            nopears.append('Orange')
        else:
            nopears.append(i)
    print(nopears)
    for i in lst[::]:
        x = ''
        while (x != "yes" and x != "no"):
            x = input('Do you like ' + i + '?')
        if x == "no":
            while i in lst:
                lst.remove(i)
    print(lst)
fruitspt2()

def fruitspt3():
    lst = ['Apple', 'Pear', 'Orange' , 'Peach', 'Cherry', 'Banana' , 'Strawberry']
    revlet = []
    nodup = []
    for i in lst:
        revlet.append(i[::-1])
    print (revlet)
    del lst[-1]
    print(lst)
    del revlet[2]
    print(revlet)
    for i in lst:
        if i not in nodup:
            nodup.append(i)
    print(nodup)
    lst.sort()
    print(lst)
fruitspt3()


