# Mirror a string
# Isabelle Kwan
# Novemver 21, 2022

def mirror(mystring):
    if len(mystring) == 1:
        return mystring
    else:
        newString = ""
        newString += mystring[-1] + mirror(mystring[:-1])
        
    return newString

print(mirror("birthday"))

# OR

def mirror(mystring):
    if len(mystring) == 0:
        return mystring
    else:
        mirror(mystring[1:]) + mystring[0]
