#!/usr/bin/python3
"""function that prints a text with 2
new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """return text with two new lines"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    # Skip leading spaces
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            # Skip spaces after punctuation
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
