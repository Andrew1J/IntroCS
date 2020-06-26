tallmountains = {'Mount Everest': 29029, 'K2': 28251, 'Lhotse':27940, 'Makalu':27838, 'Cho Oyu':26906}
#This prints out the mountain names
for key in tallmountains:
    print(key)
#This prints out the mountain heights    
for key in tallmountains:
    print(tallmountains[key])
#This prints out a sentence describing the mountains height
for key in tallmountains:
    print(key, ' is ', tallmountains[key], ' feet tall.')
#This prints out the sentences describing the mountains height, but in alphabetical order
for key in sorted(tallmountains):
    print(key, ' is ', tallmountains[key], ' feet tall.')

