def flip_case(phrase, to_swap):
    to_swap_upper = to_swap.upper()
    to_swap_lower = to_swap.lower()
    new_phrase = ''
    for letter in phrase:
        if letter == to_swap_lower:
            letter = to_swap_upper
            new_phrase += letter
        elif letter == to_swap_upper:
            letter = to_swap_lower
            new_phrase += letter
        else:
            new_phrase += letter
    return new_phrase

    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
