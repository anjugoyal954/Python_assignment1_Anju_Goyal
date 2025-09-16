n = int(input("Enter a positive integer: "))

if n < 0:
    print("Please enter a positive integer")
else:
    total = 0
    original = n   
    
    while n > 0:
        digit = n % 10      
        total = total + digit      
        n = n // 10      

    print(f"The sum of digits of {original} is {total}")
