# Example file for Programming Foundations: Algorithms by Joe Marini
# Implement a quicksort


items = [20, 6, 8, 53, 56, 23, 87, 41, 49, 19]


def quickSort(dataset, first, last):
    if first < last:
        # calculate the split point
        pivotIdx = partition(dataset, first, last)

        # now sort the two partitions
        quickSort(dataset, first, pivotIdx-1)
        quickSort(dataset, pivotIdx+1, last)


def partition(datavalues, first, last):
    # TODO: choose the first item as the pivot value
    pivotValue = datavalues[first]
    
    # TODO: establish the upper and lower indexes
    lower = first + 1
    upper = last

    # start searching for the crossing point
    done = False
    while not done:
        # TODO: advance the lower index
        while lower <= upper and datavalues[lower] <= pivotValue:
            lower = lower + 1
            
        # TODO: advance the upper index
        while datavalues[upper] >= pivotValue and upper >= lower:
            upper -= 1

        # TODO: if the two indexes cross, we have found the split point
        if upper < lower:
            done = True
        else:
            #swap
            temp = datavalues[upper]
            datavalues[upper] = datavalues[lower]
            datavalues[lower] = temp

    # TODO: when the split point is found, exchange the pivot value
    temp = datavalues[first]
    datavalues[first] = datavalues[upper]
    datavalues[upper] = temp
    
    # TODO: return the split point index
    return upper

# test the merge sort with data
print(items)
quickSort(items, 0, len(items)-1)
print(items)
