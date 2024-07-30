word=input("Enter the string:")
reverse_str=" "
for i in range(len(word)-1,-1,-1):
    reverse_str+=word[i]
print(reverse_str)    
