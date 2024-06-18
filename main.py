nums = [x for x in range(11)]
operations = ['+', '-', '*', '/']

expression = list(input().split())

def main(expression):
    flag = True
    try:
        a, c, b = expression
        a, b = int(a), int(b)
        if a not in nums or b not in nums or c not in operations:
            raise ValueError

    except ValueError:
        print('формат математической операции не соответствует заданному')

    else:
        if c == '+':
            result = a + b
        elif c == '-':
            result = a - b
        elif c == '*':
            result = a * b
        elif c == '/':
            try:
                result = a // b
            except ZeroDivisionError:
                print('на 0 делить нельзя!')
                flag = False

        if flag == True:
            print(result)

main(expression)
