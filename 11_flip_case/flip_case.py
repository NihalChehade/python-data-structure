def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    swaped_str = ""
    for char in phrase:
        if char.lower() == to_swap.lower():
          swaped_char = char.swapcase()
          swaped_str += swaped_char
        else : swaped_str += char

    return swaped_str

    

   