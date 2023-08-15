num = input("Enter your number to see if it is a palindrome: ")

palindrome = False
for i in range(0,len(num)):
    if(num[i] == num[-i-1]):
        palindrome = True
    else:
        palindrome = False
        break;

print(palindrome)

