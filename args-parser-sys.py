import argparse
import sys

def arg():
	parser = argparse.ArgumentParser()
	parser.add_argument("--number1", type=float
,default = 1.0, help = "Choose to first number Default 1")
	parser.add_argument("--number2", type=float, default = 1.0, help = "The second number Default 1")
	parser.add_argument("--operation", type=str, default = "mul", help = "Choose the operation Default add")
	args = parser.parse_args()
	sys.stdout.write(str(calc(args)))

def calc(args):
	if args.operation == "add":
		return args.number1 + args.number2
	if args.operation == "div":
		return args.number1 / args.number2
	if args.operation == "mul":
		return args.number1 * args.number2
	if args.operation == "sub":
		return args.number1 - args.number2

if __name__ == "__main__":
	arg()
