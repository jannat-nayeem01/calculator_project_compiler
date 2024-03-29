def evaluate_expression(expression):
    operator_stack = []
    operand_stack = []
    postfix_expression = []
    prefix_expression = []  # New list for storing prefix expression

    precedence = {'+': 2, '*': 1}

    def apply_operator(operator_stack, operand_stack):
        if len(operand_stack) < 2:
            raise ValueError("Insufficient operands to apply operator")

        operator = operator_stack.pop()
        operand2 = operand_stack.pop()
        operand1 = operand_stack.pop()
        if operator == '+':
            result = operand1 + operand2
        elif operator == '*':
            result = operand1 * operand2
        else:
            raise ValueError("Invalid operator")

        operand_stack.append(result)
        postfix_expression.append(operator)
        prefix_expression.append(operator)  # Add operator to prefix expression

    for token in expression:
        if token.isdigit():
            operand_stack.append(int(token))
            postfix_expression.append(token)
            prefix_expression.append(token)  # Add operand to prefix expression
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack[-1] != '(':
                apply_operator(operator_stack, operand_stack)
            operator_stack.pop()  # Remove '(' from the operator stack
        else:
            # Operator
            while operator_stack and precedence.get(operator_stack[-1], 0) >= precedence.get(token, 0):
                apply_operator(operator_stack, operand_stack)
            operator_stack.append(token)

    while operator_stack:
        apply_operator(operator_stack, operand_stack)

    return operand_stack[-1], ' '.join(postfix_expression), ' '.join(prefix_expression[::-1])  # Reverse prefix expression to get correct order
