#print the program title 

print("Check if a string is a palindrome")

# get the input sting from the user

text = input("Enter a string:")
text =text.upper()

left_index = 0
right_index= len(text) - 1

ispalindrome = True

while left_index < right_index:
    if text[left_index] != text[right_index]:
        ispalindrome = False
        break
    left_index += 1
    right_index -= 1

#print the result

if ispalindrome is True:
    print(f'The string {text} is a palindrome')
else:
    print(f'The string {text} is not a palindrome')
