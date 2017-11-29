#!/usr/bin/python3.5
# Author: Martin Brom


def read_text(filename):
    f = open(filename, 'r')
    text = f.read()
    f.close()
    return text


def find(needle, haystack):
    lh = len(haystack)
    ln = len(needle)

    i = 0
    while i < lh:
        j = 0
        while j < ln:
            if needle[j] is not haystack[i+j]:
                j = -1
                break

            j += 1

        if j is not -1:
            return i

        i += 1

    return -1


needle1 = 'God'
needle2 = 'Let there be light'
needle3 = 'And Jesus came and spake unto them'
needle4 = 'Go ye therefore, and teach all nations, baptizing them in the'
bible = read_text('bible.txt')

print(find(needle1, bible))

print(find(needle2, bible))

print(find(needle3, bible))

print(find(needle4, bible))