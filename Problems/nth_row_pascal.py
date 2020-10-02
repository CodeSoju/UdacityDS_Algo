def nth_row_pascal(n):
    if n == 0:
        return [1]
    
    current_row = [1]
    
    for i in range(1, n +1):
        prev_row = current_row
        current_row = [1]
        print("Value of i: ", i)

        for j in range(1, i):
            print(prev_row[j], prev_row[j-1])
            next_number = prev_row[j] + prev_row[j-1]
            print("Value of next num: ", next_number)
            current_row.append(next_number)
            print("value of j:", j)
            print(current_row)
        current_row.append(1)
    return current_row

print(nth_row_pascal(4))