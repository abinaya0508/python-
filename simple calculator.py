while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Exponentiate")
    choice = input("Enter choice (1/2/3/4/5/6): ")

    if choice in ('1', '2', '3', '4', '5', '6'):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        
        if choice == '1':
            result = num1 + num2
            print(result)
        elif choice == '2':
            result = num1 - num2
            print(result)
        elif choice == '3':
            result = num1 * num2
            print(result)
        elif choice == '4':
                result = num1 / num2
                print(result)
        elif choice == '5':
            result = num1 % num2
            print(result)
        elif choice == '6':
            result = num1 ** num2
            print(result)

