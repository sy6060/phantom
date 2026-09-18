#palindrome number
a=int(input("Enter a number: "))
temp=a
rev=0
while(a>0):
    dig=a%10
    rev=rev*10+dig
    a=a//10
if rev==temp:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")