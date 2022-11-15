# Q1a
def factorial(num):
    if (num < 0):
        return 'invalid'
    elif (num <= 1):
        return 1
    else:
        i = 1
        for it in range(1,num+1):
            # if (num % it == 0):
                # print(f'{it} is a factor of {num}')
            i = i * it
        return i

# Test cases
assert factorial(-5) == 'invalid'
assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(5) == 120
assert factorial(4) == 24


# Q2
def guess_me(date):
    arr = range(1,32,1)
    if date not in arr:
        return 'Invalid Date'
    low = 0
    high = len(arr) - 1
    iterator = 0
    while low <= high:
        mid = (low + high) // 2
        iterator += 1
        if arr[mid] < date:
            low = mid + 1
        elif arr[mid] > date:
            high = mid - 1
        else:
            return iterator
    return iterator

# Test cases
assert guess_me(44) == 'Invalid Date'
assert guess_me(1) == 5
assert guess_me(31) == 5
assert guess_me(24) == 2
assert guess_me(17) == 5

