# write a functin that takes in an array as input and, removes any duplicates found in an array and returns the resulting array without duplicates

def arrayCheck(array):
    result_list = []
    for num in array:
        if num not in result_list:
            result_list.append(num)
    print(result_list)
     
# array = [2, 4, 10, 20, 5, 2, 20, 4]
# arrayCheck(array)