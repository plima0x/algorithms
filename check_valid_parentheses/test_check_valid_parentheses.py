from main import valid_parentheses


def test_valid_brackets():
    brackets_list = ["[]{}()", "(){[]}", "([{}])", "{[]}()", "((([])))"]
    for bracket in brackets_list:
        assert valid_parentheses(bracket)


def test_invalid_brackets():
    brackets_list = ["[][](", "{}{}}", "()({})({{", "{}{}({}", "[][[[{]])", "())"]
    for bracket in brackets_list:
        assert not valid_parentheses(bracket)


def test_invalid_input():
    brackets = "abbcds"
    assert not valid_parentheses(brackets)


if __name__ == "__main__":
    test_valid_brackets()
    test_invalid_brackets()
    test_invalid_input()
