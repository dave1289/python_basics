def vowel_count(phrase):
    vowels = ['a', 'e','i','o','u']
    low_phrase = phrase.lower()
    results = {}
    for letter in low_phrase:
        if letter in vowels and letter not in results:
            results[letter] = 1
        elif letter in vowels and letter in results:
            results[letter] += 1
    return results

    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """