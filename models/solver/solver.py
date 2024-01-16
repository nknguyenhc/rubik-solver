def solve(cube):
    """Given a cube configuration with 6 distinct colours,
    returns a sequence of steps to solve the cube.

    The `cube` is given as a numpy array of 6 x 3 x 3,
    where each 3 x 3 block represents a face.
    Each value in the numpy array is an integer between 0 to 5 (inclusive),
    representing the colour ID that the corresponding cell has.

    The returned solution is a python list, where each element is one of
    "L", "L'", "R", "R'", "F", "F'", "B", "B'", "U", "U'", "D", "D'",
    each element represents a Rubik's cube step that rotates a face
    in clockwise direction (without an apostrophe ')
    or anticlockwise direction (with an apostrophe ').
    """
    pass
