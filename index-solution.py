#!/usr/bin/env python3

"""
Stanford CS106A Index Example
Nick Parlante
Shows reading all the words out of a file,
building a "nested" dict structure to analyze them,
printing out the contents of a dict with a standard
sorted(d.keys()) loop.
"""

import sys


"""
We'll say that an "index" dict has a key for the lowercase
version of every word in a text, and its value
is a list of all the lines where that word appears.
"""


def index_line(index, line):
    """
    Given an index dict and a line of text,
    update the index with the text of that line
    and return the modified dict.
    Use the lowercase form of each word as the key.
    >>> index_line({}, 'tea time')
    {'tea': ['tea time'], 'time': ['tea time']}
    >>> index_line({'tea': ['tea time'], 'time': ['tea time']}, 'coffee time')
    {'tea': ['tea time'], 'time': ['tea time', 'coffee time'], 'coffee': ['coffee time']}
    """
    words = line.split()
    for word in words:
        word = word.lower()
        # Your code here - update index for each word
        pass
        if word not in index:
            index[word] = []
        lines = index[word]  # Style idea: decomp by var
        lines.append(line)
    return index
    # Extension: avoid listing a line mult times per word:
    #   if line not in lines: lines.append(line)


def index_file(filename):
    """
    (provided)
    Given filename, build and return index of its contents.
    (just calls index_line() for every line)
    """
    # Build the index with every line from file
    index = {}
    with open(filename, 'r') as f:
        for line in f:
            index_line(index, line)
            # Each call to index_line() modifies the index dict
    return index


def print_index(index):
    """
    (provided)
    Given index dict, print out its contents.

    Print out the words in alphabetical order.
    Each word with **'s as shown below,
    followed by all the lines where that word appears,
    followed by a blank line.
    e.g. here is part of the gettysburg address index output

    **who**
    portion of that field, as a final resting place for those who here
    who struggled here, have consecrated it, far above our poor power to
    who fought here have thus far so nobly advanced. It is rather for us

    **will**
    add or detract. The world will little note, nor long remember what we
    """
    # Standard loop to dump out a dict by going through
    # all the keys in sorted order.
    for word in sorted(index.keys()):
        print('**' + word + '**')
        lines = index[word]       # decomp by var
        for line in lines:
            print(line, end='')   # line already has \n
        print()                   # print a blank line


def main():
    args = sys.argv[1:]
    # args: -filename-   - prints index of that text file
    if len(args) == 1:
        index = index_file(args[0])
        print_index(index)


if __name__ == '__main__':
    main()
