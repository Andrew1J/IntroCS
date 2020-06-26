data = {'a':1, 'b':1,  
            'c':2, 'd':3, 'f':4} 
result = {}
for key,value in data.items():
    if value not in result.values():
        result[key] = value
print(result)

emptyornot = not bool(data)
print(emptyornot)

print(sorted(data, key=data.get, reverse = True)[:3])
                                    
