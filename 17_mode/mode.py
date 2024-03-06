def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    count_max = 0
    letter_count_dic ={}
    for num in nums:
        count = nums.count(num)
        letter_count_dic[num] = count

    highest_count =max(letter_count_dic.values())

    for (k, v) in letter_count_dic.items():
        if v == highest_count:
            return k


