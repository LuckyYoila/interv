# write a function that takes in an array and returns true if the array has any duplicate and false if the array doesn't have a duplicate value

def arrayCheck(array):
    test_list = []
    for num in array:
        if num not in test_list:
            test_list.append(num)
    if result_list == array:
        print(False)
    else:
        print(True)

michaelchunox