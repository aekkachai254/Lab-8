value = [29,10,14,37,14,20,7,16,12]

def p2(arr, low, high):
    '''1 Hoare'''
    pivot = arr[low]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]

def quickSort(arr, low, high):
    if low < high:
        pi = p2(arr, low, high)

        quickSort(arr, low, pi)
        quickSort(arr, pi + 1, high)
    return arr

def main():
    print('quicksort : Hoare')
    '''1 Hoare'''
    arr = value.copy()
    print(quickSort(arr, 0, len(arr) - 1))

if __name__ == "__main__":
    main()