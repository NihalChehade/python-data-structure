def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    phrase_set = set(phrase)
    phrase_dic = {}
    for letter in phrase_set:
        count = phrase.count(letter)
        phrase_dic[letter] = count

    return  phrase_dic