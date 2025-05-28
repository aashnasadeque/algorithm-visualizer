import time
import matplotlib.pyplot as plt
from algorithms.sorting import quicksort, mergesort, heapsort, bubblesort, timsort, radix_sort
from algorithms.datasets.dataset_generator import generate_dataset

def measure_time(algorithm, data):
    """
    Measures the execution time of an algorithm on a dataset.
    """
    start_time = time.time()
    algorithm(data)
    end_time = time.time()
    return end_time - start_time

def get_user_input():
    """
    Prompts the user to input dataset size, order, and additional options.
    """
    print("Customize Dataset")
    size = int(input("Enter dataset size (e.g., 100, 500, 1000): "))
    order = input("Enter dataset order (random, sorted, reversed): ").strip().lower()
    if order not in ["random", "sorted", "reversed"]:
        print("Invalid order! Defaulting to 'random'.")
        order = "random"

    even_only = False
    value_range = (0, 10000)
    if order == "random":
        even_only = input("Generate only even numbers? (yes/no): ").strip().lower() == "yes"
        range_input = input("Enter value range as min,max (e.g., 0,1000): ").strip()
        value_range = tuple(map(int, range_input.split(',')))

    return size, order, value_range, even_only

def visualize():
    """
    Visualizes the performance of sorting algorithms on the given dataset.
    """

    size, order, value_range, even_only = get_user_input()


    print(f"Generating a {order} dataset of size {size}...")
    data = generate_dataset(size, order, value_range, even_only)

    algorithms = {
        "Quicksort": quicksort,
        "Mergesort": mergesort,
        "Heap Sort": heapsort,
        "Bubble Sort": bubblesort,
        "TimSort": timsort,
        "Radix Sort": radix_sort,
    }
    complexities = {
        "Quicksort": "O(n log n)",
        "Mergesort": "O(n log n)",
        "Heap Sort": "O(n log n)",
        "Bubble Sort": "O(n^2)",
        "TimSort": "O(n log n)",
        "Radix Sort": "O(nk)",
    }


    results = {}
    for name, algo in algorithms.items():
        print(f"Running {name}...")
        elapsed_time = measure_time(algo, data[:])
        results[name] = elapsed_time


    plt.figure(figsize=(10, 6))
    for name, elapsed_time in results.items():
        plt.bar(name, elapsed_time, label=f"{name} ({complexities[name]})")


    plt.title("Algorithm Performance Comparison")
    plt.xlabel("Algorithm")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.savefig("algorithm_performance.png")
    print("Graph saved as 'algorithm_performance.png'")
    plt.show()

if __name__ == "__main__":
    visualize()
