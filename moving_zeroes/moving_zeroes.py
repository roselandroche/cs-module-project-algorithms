'''
U
Input: a List of integers (positive or negative)
Returns: a List of integers (altered list)

Move non-zero integers to the left **OR** move zeroes to the right
Alter in place or create 'results' list

P
Iterate through int with loop
If int == 0
    pop int
    append 0
return array
'''

def moving_zeroes(arr):
    # Your code here
    for num in range(len(arr) - 1):
        if arr[num] == 0:
            arr.pop(num)
            arr.append(0)
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")