string=input("Enter a word:")
string=string.casefold()
reverse=reversed(string)
if list(string) == list(reverse):
    print(string,"is palindrome")
else:
    print(string,"is not palindrome")    