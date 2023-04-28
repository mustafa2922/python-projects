
def quick_sort(array, start, end):
    if start < end:

        pivot = array[end]
        i = start-1

        for j in range(start, end):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]

        array[i+1], array[end] = array[end], array[i+1]
        i += 1

        quick_sort(array , start, i-1)

        quick_sort(array , i+1 , end)


array = [20,40,10,600,30,-30,50,10,34,6,235,45,3,2,5,47,123,4]

quick_sort(array, 0, len(array)-1)
print(array)
