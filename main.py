# python3

from collections import namedtuple
from turtle import position

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        # enumerate - skaitītājs, simbols
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, position + 1))
            

        if next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1], next):
                print(i+1)
            opening_brackets_stack.pop()
    if not opening_brackets_stack:
        print("Success")
    else:
        print(opening_brackets_stack[-1]. position)



def main():
    text = input()
    mismatch = find_mismatch(text) #vai ievaditais satur i burtu , ja satur tad sak izpildit sakot no 35 rindas
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
