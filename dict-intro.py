word=input("Enter any string : ")
dict = {'a' : 0, 'e' : 0, 'i' : 0, 'o' : 0, 'u' : 0}
for c in word :
    if c in dict :
        dict[c] += 1
print(dict)