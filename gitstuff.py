def find_vowels(letters):
    vowel_list = ["a", "e", "i", 'o', "u"]
    vowel_count = 0
    vowel = []
    for letter in letters:
        if letter in vowel_list:
            vowel_count += 1
            vowel.append(letter)
    print(str(vowel_count) + " vowels found" + str(vowel))



find_vowels("hello world")


def find_palindrome(word):
    reversed_word = word[::-1]
    if reversed_word == word:
        print(word + " is a palindrome!")

    else:
        print(word + " is not a palindrome.")

find_palindrome("hello world")