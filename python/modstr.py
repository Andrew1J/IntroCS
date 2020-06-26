def changeit():
    x = input('Word:')
    if len(x) < 3:
        return x
    elif x[-3:] == 'ing':
    	x += 'ly'
    	return x
    else:
        x += 'ing'
        return x
print(changeit())

def oddindex():
    x = input('Word:')
    return x[::2]
print(oddindex())

def repeatedchar():
    x = input('Word:')
    while x:
        print (x[0], x.count(x[0]))
        x = x.replace(x[0],'')
repeatedchar()

def repeatedchar():
    x = input('Word:')
    for i in range(len(x)):
    	print (x[i], x.count(x[i]))
repeatedchar()
