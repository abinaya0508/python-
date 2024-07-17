def reverse_string():
    string = "Python"
    length = len(string)
    reversed_string = ""
    reverse= length - 1
    while reverse >= 0:
        reversed_string += string[reverse]
        reverse -= 1
    return reversed_string
print(reverse_string()) 