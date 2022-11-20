def mode(nums):
    counts = {num : nums.count(num) for num in nums}
    highest = 0
    for num in counts:
        print(counts[num])
        if counts[num] > highest:
            highest = num
    return highest

    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
