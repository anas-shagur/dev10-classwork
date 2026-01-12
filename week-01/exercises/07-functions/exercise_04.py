# get_first_vowel returns the first vowel in a string as a char.
# 1. Complete get_first_vowel.
# If no vowel is found, return None.
def get_first_vowel(value):
    vowels = 'aeiou'
    for char in value:
        if char.lower() in vowels:
            return char
    return None


if __name__ == "__main__":
    print(get_first_vowel("magnificent"))  # Expected: a
    print(get_first_vowel("winsome"))  # Expected: i
    print(get_first_vowel("xxx"))  # Expected: None
    print(get_first_vowel("hello"))  # Expected: e

    # 2. Call get_first_vowel at least one more time.
