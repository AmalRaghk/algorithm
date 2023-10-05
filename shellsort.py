def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

if __name__ == "__main__":
    input_str = input("Enter a list of numbers separated by spaces: ")
    input_list = [int(x) for x in input_str.split()]
    shell_sort(input_list)
    print("Sorted list:", input_list)
