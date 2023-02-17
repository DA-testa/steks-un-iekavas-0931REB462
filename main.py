# python3 Aleksejs Kondratjevs 091REB462

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        # enumerate - skaitītājs, simbols
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i + 1))
            

        if next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                print(i+1)
            opening_brackets_stack.pop()
    if not opening_brackets_stack:
        print("Success")
    else:
        print(opening_brackets_stack[-1]. position)



def main():
    text = input()
    # Printing answer, write your code here
    if "I" in text:
        text = input()
        find_mismatch(text) #vai ievaditais satur i burtu , ja satur tad sak izpildit sakot no 35 rindas
        # if mismatch == 0:
        #     print("Success")

if __name__ == "__main__":
    main()
