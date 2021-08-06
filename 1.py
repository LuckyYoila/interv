# write a function that takes in 3 variables as inputs and checks if any two of the variables are equal returns true if any are equal and false if none are equal

def equalityCheck(a,b,c):
    if a == b or b == c or a == c:
        print(True)

    else:
        print(False)

