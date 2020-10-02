def add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    """
    num_str = ""
    num_int = 0
    
    for num in range(len(arr)):
        num_str += str(arr[num])
    num_int = int(num_str) + 1
    
    result = []
    for digit in str(num_int):
        result += [int(digit)]
    print(result)


add_one([0])
add_one([1,2,3])
add_one([9, 9, 9])