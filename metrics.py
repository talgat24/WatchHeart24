import math

def average(data: list) -> float:
    """
    Calculate average value of the list.

    Args:
        data (list[int]): list of integers representing heart rate samples
    Returns:
        float: a floating point value representing the average of this list
    """
    if not data:
        return []  # Return empty list if the input list is empty
    total = sum(data)
    avg = total / len(data)
    return round(avg, 2)

def maximum(data: list) -> int:
    """
    Finds the maximum value in a list of numbers.
    Args:
        data (list): A list of numbers.

    Returns:
        int: The maximum value in the list.
    """
    if not data:
        return [] # Return empty list if the input list is empty
    max_value = data[0]
    for value in data:
        if value > max_value:
            max_value = value
    return max_value


def variance(data: list) -> float:
    """
    Calculate variance of the list.

    Args:
        data (list): A list of numbers.

    Returns:
        float: The variance of the list.
    """
    if not data:
        return [] # Return empty list if the input list is empty
    avg = average(data)
    squared_diffs = [(x - avg) ** 2 for x in data]
    variance = sum(squared_diffs) / len(data)  # Population variance
    return round(variance, 2)


def standard_deviation(data: list) -> float:
    """
    Calculate standard deviation of the list.

    args:
        data (list): A list of numbers.

    Returns:
        float: The standard deviation of the list.
    """
    # Calculate population standard deviation

    if not data:
        return []  # Return empty list if the input list is empty
    var = variance(data)
    std_dev = math.sqrt(var)  # Population standard deviation
    return round(std_dev, 2)

