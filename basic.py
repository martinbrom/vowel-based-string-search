#!/usr/bin/python3.5
# Author: Martin Brom

import time


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


test_count = 10

needle1 = 'God'
needle2 = 'Let there be light'
needle3 = 'And she went, and sat her down over against him'
needle4 = 'Go ye therefore, and teach all nations, baptizing them in the'
needle5 = 'Lorem'
needle6 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
bible = read_text('bible.txt')

start_time = time.time()
for i in range(0, test_count):
    find(needle1, bible)
print('extra short needle', (time.time() - start_time) / test_count * 1000, 'ms')

start_time = time.time()
for i in range(0, test_count):
    find(needle2, bible)
print('short needle', (time.time() - start_time) / test_count * 1000, 'ms')

start_time = time.time()
for i in range(0, test_count):
    find(needle3, bible)
print('long needle at start', (time.time() - start_time) / test_count * 1000, 'ms')

start_time = time.time()
for i in range(0, test_count):
    find(needle4, bible)
print('long needle at end', (time.time() - start_time) / test_count * 1000, 'ms')

start_time = time.time()
for i in range(0, test_count):
    find(needle5, bible)
print('short non-existent needle', (time.time() - start_time) / test_count * 1000, 'ms')

start_time = time.time()
for i in range(0, test_count):
    find(needle6, bible)
print('long non-existent needle', (time.time() - start_time) / test_count * 1000, 'ms')
