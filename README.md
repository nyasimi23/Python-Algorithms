Merge Sort and Selection Sort

Introduction:

This repository provides Python implementations of two sorting algorithms: Merge Sort and Selection Sort. Sorting algorithms are essential in computer science and programming as they arrange elements in a particular order, making data processing and searching more efficient.

Merge Sort:

Merge Sort is a divide-and-conquer algorithm that breaks down the unsorted list into smaller sublists, sorts them individually, and then merges them back together to obtain the final sorted list. It recursively divides the input list until each sublist has only one element (which is, by definition, sorted), and then merges these sublists back in a sorted manner. Merge Sort has an average and worst-case time complexity of O(n log n) and requires additional memory for merging the sublists.

Implementation:

The Python implementation of Merge Sort can be found in the merge_sort.py file. The merge_sort function takes an input list and returns a new sorted list using the Merge Sort algorithm.

Selection Sort:

Selection Sort is a simple comparison-based sorting algorithm that works by repeatedly selecting the minimum (or maximum) element from the unsorted part of the list and swapping it with the first unsorted element. It repeatedly shrinks the unsorted part of the list until the entire list becomes sorted. Selection Sort has a time complexity of O(n^2) in all cases, making it inefficient for large datasets.

Implementation:

The Python implementation of Selection Sort can be found in the selection_sort.py file. The selection_sort function takes an input list and modifies it in-place to achieve the sorted order using the Selection Sort algorithm.