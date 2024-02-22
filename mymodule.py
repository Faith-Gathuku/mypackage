def top_n(items, n):
    """Return the top n items in an array, in descending order

    Args:
        items (array-like): List or array-like object.
        n (int): Number of items to return.

    Returns:
        list: Top n items in descending order.

    Examples:
        >>> top_n([8, 3, 2, 7, 4], 3)
        [8, 7, 4]
    """
    # Keep sorting until we have the top n items
    for i in range(n):
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]:  # If this item is bigger than the next item
                items[j], items[j+1] = items[j+1], items[j]  # Swap the two

    # Get the last n items
    top_n = items[-n:]
    # Return in descending order
    return top_n[::-1]

