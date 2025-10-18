def arithmetic_arranger(arithmetic_problems, calculation = False):
    if len(arithmetic_problems) > 5:
        return 'Error: Too many problems.'

    for i in arithmetic_problems:
        if '+' not in i and '-' not in i:
            return "Error: Operator must be '+' or '-'."

    for i in arithmetic_problems:
        remove_signs = i.replace('+', '').replace('-', '').replace(' ', '')
        if not remove_signs.isdigit():
            return 'Error: Numbers must only contain digits.'

    for i in arithmetic_problems:
        left, mid, right = i.split()
        if len(left) > 4 or len(right) > 4:
            return 'Error: Numbers cannot be more than four digits.'

    top_parts = []
    bottom_parts = []
    dash_parts = []
    result_parts = []

    for i in arithmetic_problems:
        left, mid, right = i.split()
        width = max(len(left), len(right)) + 2
        result = 0
        arranged = ''

        if mid == '+':
            result = int(left) + int(right)
        elif mid == '-':
            result = int(left) - int(right)

        top_parts.append(left.rjust(width))
        bottom_parts.append(mid + right.rjust(width - 1))
        dash_parts.append('-' * width)
        result_parts.append(str(result).rjust(width))

        
        top_numbers = '    '.join(top_parts)
        bottom_numbers = '    '.join(bottom_parts)
        dash_numbers = '    '.join(dash_parts)
        result_numbers = '    '.join(result_parts)

        if calculation:
            arranged = f'{top_numbers}\n{bottom_numbers}\n{dash_numbers}\n{result_numbers}'
        elif not calculation:
            arranged = f'{top_numbers}\n{bottom_numbers}\n{dash_numbers}'

    return arranged

#print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
#print(arithmetic_arranger(["1 + 2", "1 - 9380"]))
#print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
#print(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))
#print(arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]))
#print(arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]))
#print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]) )
#print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]))
#print(arithmetic_arranger(["3 + 855", "988 + 40"], True))
#print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))