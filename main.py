nums = [x for x in range(1,11)]
operations = ['+', '-', '*', '/']

expression = input()
def main(expression):
    exp_list = expression.split()
    try:
        a, c, b = exp_list
        a, b = int(a), int(b)
        if a not in nums or b not in nums or c not in operations:
            raise ValueError

    except ValueError:
        return('формат математической операции не соответствует заданному')

    else:
        if c == '+':
            return str(a + b)
        elif c == '-':
            return str(a - b)
        elif c == '*':
            return str(a * b)
        elif c == '/':
            return str(a // b)

print(main(expression))