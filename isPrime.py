number = int(input())

def is_Prime(number):
    prime = True
    if number == 1:
        prime = False
    
    if number == 2:
        prime = True
    else:
            
        for n in range(2, (number//2) + 1):
            if number % n == 0:
                prime = False
                break
    return prime

def print_Prime(number):
    prime = is_Prime(number)
    number = str(number)
    if prime == True:
        print(number + " is prime")
    else:
        print(number + " is not prime")

print_Prime(number)