# Example file for Programming Foundations: Algorithms by Joe Marini
# determine if a list is sorted


items1 = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]
items2 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def is_sorted(itemlist):
    # TODO: using the brute force method
    
    # return all(itemlist[index] <= itemlist[index + 1] for index in range(len(itemlist) - 1))
    
    for index in range(0, len(itemlist) - 1):
        if itemlist[index] > itemlist[index + 1]: return False        
    return True

print(is_sorted(items1))
print(is_sorted(items2))

