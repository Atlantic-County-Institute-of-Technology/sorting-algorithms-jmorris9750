
def insertion_sort(values):
    for step in range(1, len(values)):
        key = values[step]
        j = step - 1

        # if the current number is than the number behind it, they swap
        while j >= 0 and key < values[j]:
            values[j + 1] = values[j]
            j = j-1

        values[j + 1] = key

    return values
