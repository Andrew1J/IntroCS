mountain={'Everest': [8848, 29029],'K2':[8611,28251],'Kangchenjunga':[8586, 28169],'Lhoste':[8516,27940],'Makalu':[8485,27838]}
def mountain_height3():
    print("The name of the 5 tallest mountains:")
    for mountains in mountain:
        print(mountains)
    print("The height of the 5 tallest mountains in meters:")
    for mountains in mountain:
        print(mountain[mountains][0])
    print("The height of the 5 tallest mountains in feet:")
    for mountains in mountain:
        print(mountain[mountains][1])
    for mountains in mountain:
        print(mountains ,'is',mountain[mountains][0] ,'meters tall,', 'or',mountain[mountains][1],'feet.')
        
mountain_height3()
