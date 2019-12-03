def miniMaxSum(arr):
    arr.sort()
    print(sum(arr[:-1]), sum(arr[1:]))
