def filter_nondigits(data: list) -> list:
    """
    Filters our strings containing non-digit characters from the input list and
    converts the valid entries to integers.

    Args:
        data (list): A list of strings representing heart rate data.
    
    Returns:
        list: A list of integers representing valid heart rate data.
    """
    cleaned_data = []
    for item in data:
        item = item.strip()  # Remove leading/trailing whitespace and newline characters
        if item.isdigit():
            cleaned_data.append(int(item))
    return cleaned_data