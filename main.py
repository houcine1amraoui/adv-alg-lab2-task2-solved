import matplotlib.pyplot as plt
from sorting_algorithms import bubble_sort, selection_sort, merge_sort
from utils import get_random_arrays

sizes = [10, 15, 20, 25, 30, 35, 40, 45, 50, 
 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 
 105, 110, 115, 120, 250, 500, 750, 1000, 1500, 2000, 10000, 100000]
bubble_comparisons = []
selection_comparisons = []
merge_comparisons = []

# put your code here
arrays = get_random_arrays(sizes)

for arr in arrays:
    selection_comparisons.append(selection_sort(arr))
    bubble_comparisons.append(bubble_sort(arr))
    _, merge_count = merge_sort(arr)
    merge_comparisons.append(merge_count)


plt.plot(sizes, bubble_comparisons, label="bubble sort")
plt.plot(sizes, selection_comparisons, label="selection sort")
plt.plot(sizes, merge_comparisons, label="merge sort")
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()
