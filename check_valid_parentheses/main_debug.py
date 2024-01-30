def valid_parentheses(brackets: str):
    """
    Check if the string brackets contain valid open and closed brackets.
    :param brackets: a string containing (), [] or {}.
    :return: True if the brackets string is valid, that is, a open bracket is closed by the same type.
    # returns False otherwise.
    """
    brackets_type = {
        "(": ")",
        "[": "]",
        "{": "}",
    }
    open_brackets = []
    for letter in brackets:
        print(f"Current letter: {letter}")
        if open_brackets:
            print(f"Current open_brackets: {open_brackets}")
        if letter in brackets_type:
            open_brackets.append(letter)
        elif open_brackets:
            last_open_bracket = open_brackets.pop()
            if brackets_type[last_open_bracket] != letter:
                return False
        else:
            return False

    return len(open_brackets) == 0


test_brackets = "[]{}()[]"
print(valid_parentheses(test_brackets))
