# write a function that takes a number as input and returns true if the number is a prime number and false if it is not a prime number

def primeOrNot(n):
    if (n==1):
        print(True)
    elif (n==2):
        print(True)
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        print(True)           
