class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Стек пуст")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Стек пуст")

def is_valid_brackets(s):
    stack = Stack()
    brackets = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in brackets.values():
            stack.push(char)
        elif char in brackets.keys():
            if stack.is_empty() or stack.pop() != brackets[char]:
                return False
        else:
            continue
    return stack.is_empty()

# Примеры использования
test_cases = [
    "([]{})",  # Правильная
    "([)]",    # Неправильная
    "{[}",     # Неправильная
    "()",      # Правильная
]

for test in test_cases:
    result = is_valid_brackets(test)
    print(f"Строка '{test}' является правильной скобочной последовательностью: {result}")