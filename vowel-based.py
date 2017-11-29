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
    # p = {'a': [], 'e': [], 'i': [], 'o': [], 'u': [], 'y': []}
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


def find_position(pattern, pivot_vowel, text):
    length = len(text)
    # print(pattern)
    # print(pivot_vowel)
    # print(text)
    pivot_distance = pattern[pivot_vowel][0]
    i = 0
    while i < length:
        if i is -1:
            break
        # print(i)
        # print("testing", text[i])
        # print("against", vowels[pivot_vowel])
        if text[i] is vowels[pivot_vowel]:
            j = 0
            # print("testing pivot vowel")
            while j < len(pattern[pivot_vowel]):
                rel_dist = i-pivot_distance+pattern[pivot_vowel][j]
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
            # print("testing other vowels")
            while j < 6:
                # print("j", j)
                if j is pivot_vowel:
                    j += 1
                    continue

                k = 0
                # print("len", len(pattern[j]))
                # print("pattern", pattern)
                while k < len(pattern[j]):
                    # print("k", k)
                    rel_dist = i-pivot_distance+pattern[j][k]
                    # print("relative", rel_dist)
                    # print("testing", text[rel_dist])
                    # print("against", vowels[j])
                    if text[rel_dist] is not vowels[j]:
                        k = -1
                        # i += pivot_distance
                        break

                    k += 1

                if k is -1:
                    j = -1
                    break
                j += 1

            if j is not -1:
                return i-pivot_distance

        i += 1

    return -1


needle1 = 'university'
needle2 = 'Jesus'
text = "lorem ipsum dolor amet iver unsity univer university"
bible = read_text('bible.txt')
pattern = create_pattern(needle2)
# print(pattern)
pivot_vowel = find_pivot_vowel(pattern)
# print(vowels[pivot_vowel])
print(find_position(pattern, pivot_vowel, bible))
