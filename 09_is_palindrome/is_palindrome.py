def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    lower_phrase_list = list(phrase.lower().replace(" ", ""))
    lower_phrase_list.reverse()

    if "".join(lower_phrase_list) == phrase.lower().replace(" ", ""):
        return True
    else : return False


