# print the program name
print("Print a version of string  with each word capitalized and a full stop added at the end")
print()

#get the input from the user
x = input("Enter a string: ").lower()
i = 0
result = ''

while i < len(x):
    word = x[i]
    if word >= 'a' and word <= 'z':
        if i == 0 or (i != -1 and x[i - 1] == ' '):
            result += chr(ord(word) - 32)
        else:
            result += word
    else:
        result += word
    i += 1
if result and result[-1] != '.':
    result += '.'

print("The result will be:", result)
