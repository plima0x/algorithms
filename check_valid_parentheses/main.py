def valid_parentheses(brackets: str):
    """
    Check if the string brackets contains valid open and closed brackets.
    :param brackets: a string containing (), [] or {}.
    :return: True if the brackets string is valid, that is, an open bracket is closed by the same type.
     Returns False otherwise.
    """
    brackets_type = {
        "(": ")",
        "[": "]",
        "{": "}",
    }
    # the list open_brackets will store all the current open brackets.
    open_brackets = []
    for letter in brackets:
        # Verify if the current letter is an open bracket, that is, it is a dictionary key.
        if letter in brackets_type:
            # Store the open bracket.
            open_brackets.append(letter)
        # Otherwise, the letter is a close bracket. Then, verify if there is any open brackets.
        elif open_brackets:
            # Get the last open bracket.
            last_open_bracket = open_brackets.pop()
            # Verify if the type of the open bracket returned by the dictionary is different from the
            # current letter value. If it is, then, return False.
            if brackets_type[last_open_bracket] != letter:
                return False
        # If the current letter is a close bracket and there is no open brackets in the list,
        # then the string brackets is an invalid string.
        else:
            return False
    # If there is any element in the open_brackets list until this point, then the string brackets was invalid and
    # the comparison below will return False. Otherwise, it will return True.
    return len(open_brackets) == 0
