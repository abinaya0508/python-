num=int(input("Enter the number:"))
factorial=1
for i in range(1,num+1):
    factorial*=i
Result=f"The number of {num}'s factorial is {factorial}"
print(Result)
