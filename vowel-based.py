#!/usr/bin/python3.5
# Author: Martin Brom

vowels = ('a', 'e', 'i', 'o', 'u', 'y')


def read_text(filename):
    f = open(filename, 'r')
    text = f.read()
    f.close()
    return text


def is_vowel(char):
    return char in vowels


def create_pattern(needle):
    p = {'a': [], 'e': [], 'i': [], 'o': [], 'u': [], 'y': []}

    for i in range(0, len(needle)):
        if is_vowel(needle[i]):
            print(p)
            p[needle[i]].append(i)

    return sorted(p.iteritems(), key=len, reverse=True)


def get_pivot_vowel(pattern):
    return pattern[0]


def find_position(pattern, text):
    length = len(text)
    return -1


def read_needle():
    return 'university'


bible = read_text('bible.txt')
pattern = create_pattern(read_needle())
print(pattern)
print(find_position(pattern, bible))
