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


def vowel_index(char):
    return vowels.index(char)


def create_pattern(needle):
    p = [[], [], [], [], [], []]

    for i in range(0, len(needle)):
        if is_vowel(needle[i]):
            p[vowel_index(needle[i])].append(i)

    return p


def find_pivot_vowel(p):
    max_len = 0
    pivot_index = -1

    for i in range(0, 6):
        l = len(p[i])
        if l > max_len:
            max_len = l
            pivot_index = i

    return pivot_index


def find_position(pattern, pivot_vowel, text, needle):
    length = len(text)
    pivot_distance = pattern[pivot_vowel][0]
    i = 0
    while i < length:
        if i is -1:
            break
        if text[i] is vowels[pivot_vowel]:
            j = 0
            while j < len(pattern[pivot_vowel]):
                rel_dist = i - pivot_distance + pattern[pivot_vowel][j]
                if rel_dist >= length:
                    i = -1
                    break

                if text[rel_dist] is not vowels[pivot_vowel]:
                    i += pivot_distance + 1
                    j = -1
                    break

                j += 1

            if j is -1:
                continue

            j = 0
            while j < 6:
                if j is pivot_vowel:
                    j += 1
                    continue

                k = 0
                while k < len(pattern[j]):
                    rel_dist = i - pivot_distance + pattern[j][k]
                    if text[rel_dist] is not vowels[j]:
                        k = -1
                        break

                    k += 1

                if k is -1:
                    j = -1
                    break
                j += 1

            k = 0
            if j is not -1:
                while k < len(needle):
                    if text[i-pivot_distance+k] is not needle[k]:
                        k = -1
                        break

                    k += 1

                if k is not -1:
                    return i-pivot_distance

        i += 1

    return -1


needle1 = 'God'
needle2 = 'Let there be light'
needle3 = 'And Jesus came and spake unto them'
needle4 = 'Go ye therefore, and teach all nations, baptizing them in the'
bible = read_text('bible.txt')

pattern = create_pattern(needle1)
pivot_vowel = find_pivot_vowel(pattern)
print(find_position(pattern, pivot_vowel, bible, needle1))

pattern = create_pattern(needle2)
pivot_vowel = find_pivot_vowel(pattern)
print(find_position(pattern, pivot_vowel, bible, needle2))

pattern = create_pattern(needle3)
pivot_vowel = find_pivot_vowel(pattern)
print(find_position(pattern, pivot_vowel, bible, needle3))

pattern = create_pattern(needle4)
pivot_vowel = find_pivot_vowel(pattern)
print(find_position(pattern, pivot_vowel, bible, needle4))
