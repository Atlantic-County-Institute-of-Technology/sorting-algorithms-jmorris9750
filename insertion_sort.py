# def insertion_sort(values):
#     for i in range(len(values)):
#         current_value = values.pop(i)
#         while j >= 0 and current_value < values[j]:
#
#     return values
def insertionSort(values):
    for step in range(1, len(values)):
        key = values[step]
        j =step - 1

        while j>= 0 and key < values[j]:
            values[j + 1] = values[j]
            j=j -1

        values[j +1] = key

print('sorted Array in Ascending Order:')
print(insertionSort)