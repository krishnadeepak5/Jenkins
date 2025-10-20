# Testing the automated build trigger from GitHub


    Args:
        length (int/float): The length of the rectangle.
        width (int/float): The width of the rectangle.

    Returns:
        int/float: The calculated area.
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive.")
    return length * width

# This block is for local execution, but not strictly needed for Jenkins CI
if __name__ == '__main__':
    try:
        result = calculate_area(10, 5)
        print(f"Area calculated: {result}")
    except ValueError as e:
        print(f"Error: {e}")
