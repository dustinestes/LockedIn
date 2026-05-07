from stack import Stack


def is_balanced(input_str):
    stack = Stack()
    for item in input_str:
        if item == "(":
            stack.push(item)
            continue
        if item == ")":
            if stack.pop() is None:
                return False


    if stack.size() == 0:
        return True
    return False

