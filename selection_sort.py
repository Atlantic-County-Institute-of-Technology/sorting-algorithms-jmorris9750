def selection_sort(values):
    i = 0
    j = 0
    min_num = i
    for x in range(len(values)-1):
        j = j + 1
        i = i - 1
        if values[j] < values[min_num]:
            min_num = j
        values[i],values[min_num] = values[min_num],values[i]
    return values
