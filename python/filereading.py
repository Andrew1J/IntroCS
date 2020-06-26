def readall():  
    test_file = open('/Users/andrewjuang/test.txt')
    text = test_file.read()
    print(text)
readall()

def readfirstn(n):
    test_file = open('/Users/andrewjuang/test.txt','r')
    for i in range(n):
        line = test_file.readline()
        print(line)
    test_file.close()
readfirstn(3)

def readlastn(n):
    test_file = open('/Users/andrewjuang/test.txt','r')
    lines = test_file.readlines()[-n:]
    for line in lines:
        print(line)
    test_file.close()
readlastn(3)

def linesinlist():
    test_file = open('/Users/andrewjuang/test.txt','r')
    lines = test_file.readlines()
    x = []
    for line in lines:
        x.append(line)
    print(x)
linesinlist()

def countlines():
    count = 0
    test_file = open('/Users/andrewjuang/test.txt','r')
    for line in test_file:
        count += 1
    print('Line Count:', count)
countlines()
