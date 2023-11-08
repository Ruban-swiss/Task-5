str = input("Enter the string:") 
for i in range(len(str) // 2): 
    if str[i] != str[1 - i]: 
        print('it is ot a Palindrome') 
        break 
else:
    print('it is a Palindrome') 