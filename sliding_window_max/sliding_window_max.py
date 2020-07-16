'''
U
Input: a List of integers as well as an integer `k` representing 
    the size of the sliding window
Returns: a List of integers

The window is k blocks wide.
The window covers list int of amount k.
Window moves from left to right one block/list item at a time.
Returned value of list, of max values of items covered by window as it moves.

P
Create mini list (aka window)
Move window through array
Call max at first position
As moves to the right, re-get max
If it is, new max added to results
If list ends, return results
'''
def sliding_window_max(nums, k):
    # Your code here
    result = []
    start = 0
    end = k

    while end <= len(nums):
        window = nums[start:end]
        max_num = max(window)
        result.append(max_num)
        start+=1
        end+=1

    return result

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
