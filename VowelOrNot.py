#(4)VOWEL OR NOT

while True:
    print("Enter '0' for exit.")
    ch = input("Enter any character: ")
    try:
        ch = str(ch)
    except:
        print('error, try again')
        continue
    if ch == '0':
        break
    else:
        if(ch=='a' or ch=='A' or ch=='e' or ch=='E' or ch=='i' or ch=='I' 
        or ch=='o' or ch=='O' or ch=='u' or ch=='U'):
            print(ch, "is a vowel.")
        else:
            print(ch, "is not a vowel.")