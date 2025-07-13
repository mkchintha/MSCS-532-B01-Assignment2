import time
import random
import tracemalloc
import sys
sys.setrecursionlimit(2000)

# Merge Sort Implementation
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# Quick Sort Implementation
def quick_sort(arr):
    def partition(low, high):
        # Randomly select a pivot index and swap with the last element
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort_rec(low, high):
        if low < high:
            pi = partition(low, high)
            quick_sort_rec(low, pi - 1)
            quick_sort_rec(pi + 1, high)

    quick_sort_rec(0, len(arr) - 1)
    return arr


# Measure performance
def measure_performance(sort_func, data):
    tracemalloc.start()
    start = time.time()
    result = sort_func(data.copy())
    end = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return {
        "result": result,
        "time_ms": (end - start) * 1000,
        "memory_kb": peak / 1024
    }

# Dataset generation
def generate_datasets(size=1000):
    sorted_data = list(range(size))
    reverse_sorted_data = list(range(size, 0, -1))
    random_data = random.sample(range(size), size)
    return sorted_data, reverse_sorted_data, random_data

# Run all benchmarks
def benchmark():
    sizes = [1000]
    for size in sizes:
        sorted_data, reverse_sorted_data, random_data = generate_datasets(size)

        print(f"\nDataset Size: {size}\n")

        for name, data in [("Sorted", sorted_data), ("Reverse Sorted", reverse_sorted_data), ("Random", random_data)]:
            print(f"--- {name} ---")
            for algo_name, func in [("Merge Sort", merge_sort), ("Quick Sort", quick_sort)]:
                metrics = measure_performance(func, data)
                print(f"{algo_name}: Time = {metrics['time_ms']:.2f} ms, Memory = {metrics['memory_kb']:.2f} KB")

benchmark()
