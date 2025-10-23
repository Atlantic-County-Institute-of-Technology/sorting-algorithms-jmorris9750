def selection_sort(values):
    j = 0
    for i in range(len(values)-1):
        j = j + 1
        min_num = i
        for j in range(i+1, len(values)):
            if values[j] < values[min_num]:
                min_num = j

        values[i], values[min_num] = values[min_num], values[i]

    return values
