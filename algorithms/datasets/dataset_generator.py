import numpy as np

def generate_dataset(size, order="random", value_range=(0, 10000), even_only=False):
    """
    Generates a dataset with specified size, order, and properties.

    Returns:
        list: Generated dataset.
    """
    if order == "random":
        data = [np.random.randint(value_range[0], value_range[1]) for _ in range(size)]
        if even_only:
            data = [x if x % 2 == 0 else x + 1 for x in data]
    elif order == "sorted":
        data = list(range(value_range[0], value_range[0] + size))
    elif order == "reversed":
        data = list(range(value_range[0] + size, value_range[0], -1))
    else:
        raise ValueError("Invalid order type. Choose 'random', 'sorted', or 'reversed'.")
    return data

if __name__ == "__main__":
    print("Random dataset:", generate_dataset(10, order="random", value_range=(0, 100), even_only=False))
    print("Random even dataset:", generate_dataset(10, order="random", value_range=(0, 100), even_only=True))
    print("Sorted dataset:", generate_dataset(10, order="sorted", value_range=(0, 100)))
    print("Reversed dataset:", generate_dataset(10, order="reversed", value_range=(0, 100)))
