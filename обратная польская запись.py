def calculate_rpn(expression):
    stack = [] #создаём пустой стек
    tokens = expression.split()

    for token in tokens:
        try:
            operand = int(token)
            stack.append(operand)
        except ValueError:
            if token in ['+', '-', '*', '/']:
                operand2 = stack.pop()
                operand1 = stack.pop()
                if token == '+':
                    result = operand1 + operand2
                elif token == '-':
                    result = operand1 - operand2
                elif token == '*':
                    result = operand1 * operand2
                elif token == '/':
                    result = int(operand1 / operand2) # Обработка целочисленного деления
                stack.append(result)
            else:
                raise ValueError(f"Неверный токен: {token}")

    if len(stack) != 1:
        raise ValueError("Неверная запись выражения")
    return stack[0]


try:
    expression = "4 2 * 3 +"
    result = calculate_rpn(expression)
    print(f"Результат: {result}")

    expression = "4 2 3 * +"
    result = calculate_rpn(expression)
    print(f"Результат: {result}")


    expression = "10 5 -"
    result = calculate_rpn(expression)
    print(f"Результат: {result}")

    expression = "4 2 +"
    result = calculate_rpn(expression)
    print(f"Результат: {result}")
except ValueError as e:
    print(f"Ошибка: {e}")



