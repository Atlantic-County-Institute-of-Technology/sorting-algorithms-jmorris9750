def bubble_sort(values):


    # from main import outer_pass, inner_pass
    outer_pass =0
    inner_pass= 0




    for i in range(len(values) - 1):
        outer_pass += 1
        # assume the final value in each pass is sorted
        for j in range(len(values) -i - 1):
            inner_pass += 1
            # perform the swap using a temp variable
            if values[j] > values[j+1]:
                values[j], values[j+1] = values[j+1], values[j]
                # temp = values[j]
                # values[j] = values[j+1]
                # values[j+1] = temp
    return values
