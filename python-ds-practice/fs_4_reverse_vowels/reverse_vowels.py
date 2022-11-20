def reverse_vowels(s):
    vowels = []
    vowel_index = []
    end = []
    for i in range(len(s)):
        if s[i] in ['a', 'e', 'i', 'o', 'u']:
            vowels.append(s[i])
            vowel_index.append(i)
    vowels = vowels[::-1]
    ind = 0
    for i in range(len(s)):
        if i in vowel_index:
            end.append(vowels[ind])
            ind += 1
        else:
            end.append(s[i])
    new_str = ''
    return new_str.join(end)


    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
