def draw(i):
    """
    A simple helper function that returns a string representation of the number `i`
    with the correct amount of leading spaces.

    Parameters:
        i (int): The number to draw (must be greater than 0).

    Returns:
        str: A string containing `i` preceded by two spaces for each level before it.
    """
    assert(i > 0)
    return


def make_wave(n, h):
    """
    Generates a number wave pattern based on two positive integers n and h.

    The pattern increases from 1 up to n, then decreases back down to 1,
    repeating until a total of h lines are generated.
    Each number is drawn using the draw() helper function, which ensures proper spacing.

    Parameters:
        n (int): The highest number in the wave (must be positive).
        h (int): The total number of lines to generate (must be positive).

    Returns:
        str: A string representing the wave pattern, with each line separated by '\n'.
    """

    res = ""  # the result string


    return res