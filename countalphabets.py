def count_alphabets(x):
    count1=0
    count2=0
    for el in x :
        if el.isalpha():
            count1+=1
    for el in x :
        if el.isdigit():
            count2+=1
    print("DIGITS OF NUMBERS IN STRING ARE EQUAL TO ",count2)
    
    print("ALPHABETS OF STRING ARE EQUAL TO ",count1)
string =input("ENTER STRING : ")
count_alphabets(string)           
        