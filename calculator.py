#!/usr/bin/env python3


def calculate(user_input):
	parsed_input = parse(user_input)
	try:
		subtotal = divide_and_multiply(parsed_input)
		return add_and_subtract(subtotal)

	except DivideByZero:
		print("Divide by zero error")

def parse(user_input):
	return True

def divide_and_multiply(parsed_input):
	return True

def add_and_subtract(subtotal):
	return True

def main():
	print("Fractions Calculator")

	while True:
		try:
			user_input = input("Enter problem:")
			result = calculate(user_input)
			print(result)
		
		except ParseError, :
			print("wrong format")
	
if __name__ == '__main__':
	main()
