def countOfArrayElement(arr):
    if not arr:
        return 0

    l = len(arr)
    max = arr[0]
    count = 1

    for i in range(1, l):
        if arr[i] == max:
            count += 1
        elif arr[i] > max:
            max = arr[i]
            count = 1

    return l - count

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(countOfArrayElement(arr))