def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    dic={}

    lowered_phrase=phrase.lower()
    for char in lowered_phrase:
        if char in 'aeiou':
            dic[char]=lowered_phrase.count(char)
    return dic