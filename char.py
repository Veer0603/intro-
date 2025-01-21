char1="AEIOUaeiou"
char2=input("Enter string : ")
count =0
for char in char2:
    if char in char1:
        count=count+1
print(count)
