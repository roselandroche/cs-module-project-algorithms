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
    result = []
    zero = 0
    for num in range(len(arr)):
        if arr[num] != 0:
            result.append(arr[num])
        elif arr[num] == 0:
            zero += 1
    for item in range(zero):
        result.append(0)
    return result


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")