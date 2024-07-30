n=int(input("Enter the number:"))
#sum of the two preceding ones, usually starting with 0 and 1.
fib_seq=[0,1]
for i in range(1,n):
    #sum of using negative idexing
    fibonacci= fib_seq[-1]+fib_seq[-2]
    fib_seq.append(fibonacci)
print(fib_seq)    