"""
026. Is Balanced.

Balanced Parentheses

Parentheses are balanced when each parenthesis has a corresponding parenthesis,
and the pairs of parentheses are properly nested. For example:

- `()`
- `()()`
- `(())`
- `((()))`
- `(()(()))`

Unbalanced Parentheses

- `(`
- `)`
- `(()`
- `(()()`
- `(()))`

Complete the `is_balanced` function.
It takes a string as input and returns `True` if the parentheses in the string
are balanced, and `False` otherwise.
Use an instance of the provided `Stack` class in `stacks.py` to keep track
of the parentheses.
"""

from stacks import Stack


def is_balanced(input_str: str) -> bool:
    """
    Solution.
    Time Complexity: O()
    Space Complexity: O()
    """
    stack: Stack = Stack()
    for c in input_str:
        if c == "(":
            stack.push(c)
        if c == ")":
            el: int | str | None = stack.pop()
            if el != "(":
                return False

    return stack.is_empty()
