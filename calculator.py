#!/usr/bin/env python3

import re
import math
from fractions import Fraction


def calculate(user_input):
    try:
        parsed_input = parse(user_input)
        subtotal = divide_and_multiply(parsed_input)
        total = add_and_subtract(subtotal)
        return str(normalize(total[0]))
    except Exception as e:
        print("Caluclation error: ", e)


def parse(user_input):
    number = '(\d*_?\d*/?\d*)'
    operator = '([\*\/\+\-])'
    leftovers = '(.*)'
    regex = '\??' + number + operator + number + leftovers
    tokenize_regex = operator + number + leftovers

    stripped = user_input.replace(" ", "")
    regex_match = re.match(regex, stripped)

    tokens = regex_match.group(1, 2, 3)
    tokenize = regex_match.group(4)
    while tokenize:
        subtokens = re.match(tokenize_regex, tokenize)
        tokens = tokens + subtokens.group(1, 2)
        tokenize = subtokens.group(3)
    return list(tokens)


def simplify_fraction(token):
    if '/' in token:
        try:
            split = token.split('/')
        except AttributeError:
            split = token
            del split[split.index('/')]
        try:
            den = split[1]
        except IndexError:
            den = 1
        num = split[0]

        if '_' in token:
            split = num.split('_')
            whole = split[0]
            print(num, den, whole)
            num = int(split[1]) + int(den) * int(whole)
        return [int(num), int(den)]
    elif '_' in token:
        raise Exception('format error, cant have whole mixed ',
                        'fraction without denominator')
    else:
        return [int(token), 1]


def get_operands(operator, equation):
    pos = equation.index(operator)
    lhs = equation[pos - 1]
    rhs = equation[pos + 1]
    return [lhs, rhs, pos]


def divide_and_multiply(equation):
    operators = ['/', '*']
    for operator in operators:
        while operator in equation:
            operands = get_operands(operator, equation)
            lhs = simplify_fraction(operands[0])
            rhs = simplify_fraction(operands[1])
            if operator == '/':
                num = int(lhs[0] * rhs[1])
                den = int(lhs[1] * rhs[0])
            else:
                num = int(lhs[0] * rhs[0])
                den = int(lhs[1] * rhs[1])
            pos = operands[2]
            equation[pos] = [num, '/', den]
            del equation[pos + 1]
            del equation[pos - 1]
    return equation


def add_and_subtract(equation):
    print(equation)
    operators = ['-', '+']
    for operator in operators:
        while operator in equation:
            operands = get_operands(operator, equation)
            lhs = simplify_fraction(operands[0])
            rhs = simplify_fraction(operands[1])
            print(lhs, rhs)
            den = math.lcm(lhs[1], rhs[1])
            lhs_num = int(den/lhs[1] * lhs[0])
            rhs_num = int(den/rhs[1] * rhs[0])
            if operator == '-':
                num = lhs_num - rhs_num
            if operator == '+':
                num = lhs_num + rhs_num
            pos = operands[2]
            equation[pos] = [num, '/', den]
            del equation[pos + 1]
            del equation[pos - 1]
    print(equation)
    return equation


def normalize(equation):
    num = equation[0]
    den = equation[2]
    if int(den) == 1:
        return num
    if den == num:
        return 1
    else:
        # used fraction module because I didn't want to write this out
        frac = Fraction(num, den)
        num = frac.numerator
        den = frac.denominator
        if num > den:
            whole = int(num / den)
            num = int(num % den)
            if num == 0:
                return whole
            else:
                return str(whole) + '_' + str(num) + '/' + str(den)
        else:
            return str(num) + '/' + str(den)


def main():
    print("Fractions Calculator")

    while True:
        try:
            user_input = input("Enter problem:")
            if user_input == 'done':
                break
            else:
                result = calculate(user_input)
                print(result)

        except KeyboardInterrupt:
            break
        except:
            print("Bad Format")
if __name__ == '__main__':
    main()
