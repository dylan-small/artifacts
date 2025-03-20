
def binary_search(arr, target):
    """
    Binary search on a sorted list to find the index of the target element.

    :param arr: A sorted list of elements.
    :param target: The element to search for.
    :return: The index of the target element if found, else -1.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

if __name__ == "__main__":
    sorted_list = [1, 3, 4, 7, 14, 11, 13, 15, 17, 19]
    target = 19

    print(binary_search(sorted_list, target))

    