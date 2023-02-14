# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i+1))
            # Process opening bracket, write your code here
            
        if next in ")]}":
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                return i+1
            opening_brackets_stack.pop()
            # Process closing bracket, write your code here
            
    if opening_brackets_stack:
        return opening_brackets_stack[-1].position
    return "Success"


def main():
    ievade = input()
    if "I" in ievade:
        text = input()
    mismatch = find_mismatch(text)
    if mismatch == "Success":
        print("Success")
    else:
        print(mismatch)
        
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
