"""
The main Python mpdule that combines cleaner and metrics functions in order to
perform comprehensive analysis
"""

from metrics import average, maximum, standard_deviation
from cleaner import filter_nondigits

import matplotlib.pyplot as plt


def run(filename: str) -> tuple:
    """
    Process heart rate data from the specified file, clean it, calculate metrics,
    and save visualizations.

    Args:
        filename (str): The path to the data file (e.g., 'data/phase0.txt').

    Returns:
        float, float, float: You will return the average, max, and standard deviation
    """ 
    data = []

    # open file using file I/O and read it into the `data` list
    with open(filename, 'r') as file:
        data = file.readlines()

    # Use `filter_nondigits` to clean the data and remove invalid entries, save the output to a new variable
        cleaned_data = filter_nondigits(data)

    # plot this data to explore changes in heart rate for this file, save this visualization to the "images" folder
    plt.figure(figsize=(10, 6))
    plt.plot(cleaned_data, marker='o', linestyle='-')
    plt.title(f'Heart Rate Data - {filename}')
    plt.xlabel('Time (5-minute intervals)')
    plt.ylabel('Heart Rate')
    plt.grid(True)

    # Save this visualization to the "images" folder
    output_image_path = f'images/{filename.split("/")[-1].replace(".txt", ".png")}'
    plt.savefig(output_image_path)
    plt.close()  # Close the plot to free memory

    # calculate the average, maximum, and standard deviation of this file using the functions you've wrote
    avg_hr = average(cleaned_data)
    max_hr = maximum(cleaned_data)
    std_dev_hr = standard_deviation(cleaned_data)

    # return all 3 values
    return avg_hr, max_hr, std_dev_hr


if __name__ == "__main__":
    # print results 
    print(run("data/phase0.txt"))

    # List of all files to process
    file_paths = [
        "data/phase0.txt",
        "data/phase1.txt",
        "data/phase2.txt",
        "data/phase3.txt"
    ]
  
  # Loop through each file and process it
    for file_path in file_paths:
        avg, max_val, std_dev = run(file_path)
        print(f"Results for {file_path}:")
        print(f"Average: {avg}, Maximum: {max_val}, Standard Deviation: {std_dev}")

        # Example use of operator library for comparisons
        print("Comparison Results:")
        print(f"Is Average > Maximum? {operator.gt(avg, max_val)}")
        print(f"Is Standard Deviation < Average? {operator.lt(std_dev, avg)}")
