capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small = "abcdefghijklmnopqrstuvwxyz"
def rot13(string):
    holder = "" 
    for a in string:
        if(a.isalpha()):
            if(a.isupper()):
                loc = capital.find(a)
                if(loc> 12):
                    add = 26 - loc
                    holder += capital[13-add]
                else:
                    add = loc + 13
                    holder += capital[add] 
            elif(a.islower()):
                loc = small.find(a)
                if(loc> 12):
                    add = 26 - loc
                    holder += small[13-add]
                else:
                    add = loc + 13
                    holder += small[add]
        else:
            holder += a
    return holder
                

print("This is a rot13 cyphering and decyphering tool.")
inpt = input("Enter the text to be cyphered or decyphered: ")
print(rot13(inpt))
