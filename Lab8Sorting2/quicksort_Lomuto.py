value = [29,10,14,37,14,20,7,16,12]

def p1(arr, low, high):
    '''0 Lomuto'''
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickSort(arr, low, high):
    if low < high:
        pi = p1(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
    return arr

def main():
    print('quicksort : Lomuto')
    '''0 Lomuto'''
    arr = value.copy()
    print(quickSort(arr, 0, len(arr)-1))

if __name__ == "__main__":
    main()