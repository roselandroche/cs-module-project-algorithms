'''
U
Input: a List of integers
Returns: a List of integers (modified)

Each integer is replaced by the product of the other integers in the list OR
    create a result arr

P
Iterate over int
Save index of current int
Multiply all int except current saved int
Append product to new arr in order
Return new arr
'''
def product_of_all_other_numbers(arr):
    # Your code here
    result = []
    product = 1
    current_int = arr[0]
    for num in range(len(arr) -1):
        if num != current_int:
            product *= arr[num]
            result.append(product)
            current_int += 1
        
    return result


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
