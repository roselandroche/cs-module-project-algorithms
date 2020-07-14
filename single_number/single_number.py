'''
U
Input: a List of integers (positive or negative)
    - every int except one shows up twice
Returns: the only integer without a double

P
For loop to iterate through integers
Use method of arr.count(int)
If the current integer count == 2, continue
If the current integer count = 1, return current integer
'''
def single_number(arr):
    # Your code here
    for num in arr:
        if arr.count(num) == 1:
            return num


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")