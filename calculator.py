#!/usr/bin/env python3

import re
import math
from fractions import Fraction


def calculate(user_input):
    parsed_input = parse(user_input)
    subtotal = divide_and_multiply(parsed_input)
    total = add_and_subtract(subtotal)
    return normalize(total[0])
    # except Exception as e:
        # print("Caluclation error: ", e)


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
    if '_' in token:
        split = token.split('_')
        whole = int(split[0])
        rest = int(split[1])
        if '/' in token:
            split = rest.split('/')
            try:
                den = split[1]
            except IndexError:
                den = 1
            num = int(split[0]) + int(den) * int(whole)
            return [int(num), int(den)]
        else:
            return [whole + rest, int(1)]
    elif '/' in token:
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
        return [int(num), int(den)]
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
                num = lhs[0] * rhs[1]
                den = lhs[1] * rhs[0]
            else:
                num = lhs[0] * rhs[0]
                den = lhs[1] * rhs[1]
            pos = operands[2]
            equation[pos] = [num, '/', den]
            del equation[pos + 1]
            del equation[pos - 1]
    return equation


def add_and_subtract(equation):
    operators = ['-', '+']
    for operator in operators:
        while operator in equation:
            operands = get_operands(operator, equation)
            lhs = simplify_fraction(operands[0])
            rhs = simplify_fraction(operands[1])
            den = math.gcd(lhs[1], rhs[1])
            lhs_num = den/lhs[1] * lhs[0]
            rhs_num = den/rhs[1] * rhs[0]
            if operator == '-':
                num = lhs_num - rhs_num
            if operator == '+':
                num = lhs_num + rhs_num
            pos = operands[2]
            equation[pos] = [num, '/', den]
            del equation[pos + 1]
            del equation[pos - 1]
    return equation


def normalize(equation):
    num = equation[0]
    den = equation[2]
    if den == 1:
        return int(num)
    else:
        # used fraction module because I didn't want to write this out
        frac = Fraction(num, den)
        num = frac.numerator
        den = frac.denominator
        if num > den:
            whole = num / den
            num = num % den
            if num == 0:
                return int(whole)
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
                print(calculate(user_input))

        except KeyboardInterrupt:
            break
        except:
            print("Bad Format")
if __name__ == '__main__':
    main()
