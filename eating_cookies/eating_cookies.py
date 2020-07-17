'''
U
Input: an integer representing amount of cookies
Returns: an integer representing number of ways to eat the cookies

Constraints:
    Cookies can be eaten 1, 2, or 3 at a time

Have to find ALL COMBINATIONS -- use recursion

P
Base case:
    number eaten == number given OR n < 2
How to get there:
    
'''

def eating_cookies(n, cache):
    # Your code here
    if n == 0:
        return 1
    if n < 0:
        return 0

    if cache[n] > 0:
        return cache[n]
    
    total_possibilities = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
    cache[n] = total_possibilities
    return total_possibilities

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
